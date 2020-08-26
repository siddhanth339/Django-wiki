from django.shortcuts import render
from django.http import Http404
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
                    "TITLE": name,
                    "content": markdown2.markdown(html)
                    })
    else:
        raise Http404("Page Not Found!")
