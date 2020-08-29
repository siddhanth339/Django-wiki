from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django import forms
from . import util
import markdown2

def index(request): # displays the main page
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def TITLE(request, name):
    """
    this method displays the page corresponding to a particular link 
    on the sidebar
    """
    html = util.get_entry(name)
    if (html != None):
        return render(request, "encyclopedia/Entry.html",{
                    "ti": name,
                    "content": markdown2.markdown(html)
                    })
    else:
        raise Http404("Page Not Found!")

def search(request):
    """
    this page also displays the page corresponding to a particular 
    link but if that page doesn't exist then it shows the Results page
    with familiar results
    """ 
    if 'q' in request.GET:
        html = util.get_entry(request.GET['q'])
        if (html != None):
            return render(request, "encyclopedia/Entry.html",{
            "ti": request.GET['q'],
            "content": markdown2.markdown(html)
            })
        else:
            available_entries = []
            query = request.GET['q'].lower()
            for entry in util.list_entries():
                if (query in entry.lower()):
                    available_entries.append(entry)
            
            return render(request, "encyclopedia/Results.html", {
                        "available_entries": available_entries
                    })

class NewPage(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={"style": "margin-left: 50px; width: 500px; height: 500px"}))

def newPage(request): # creates a new page
    if request.method == "POST":
        form = NewPage(request.POST)

        if (form.is_valid()):
            title = form.cleaned_data["title"]
            cont = form.cleaned_data["content"]
            
            util.save_entry(title, cont)

            return render(request, "encyclopedia/Entry.html",{
            "ti": title,
            "content": markdown2.markdown(util.get_entry(title))
            })
        else:
            return render(request, "encyclopedia/newPage.html", {
                "form": form
            })

    return render(request, "encyclopedia/newPage.html", {
        "form": NewPage()
    })