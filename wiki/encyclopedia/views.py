from django.shortcuts import render
from django.http import Http404, HttpResponse
from . import util

import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def TITLE(request, name):
    html = util.get_entry(name)
    if (html != None):
        return render(request, "encyclopedia/Entry.html",{
                    "ti": name,
                    "content": markdown2.markdown(html)
                    })
    else:
        raise Http404("Page Not Found!")

def search(request):
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
