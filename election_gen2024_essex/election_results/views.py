from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import GEResults

import lxml.etree as et

# Create your views here.


def results(request):
    election_results = GEResults.objects.all().values()
    template = loader.get_template("results.html")
    context = {"election_results": election_results}
    return HttpResponse(template.render(context, request))


def details(request, id):
    result = GEResults.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {"result": result}
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def fruits(request):
    template = loader.get_template("template.html")
    context = {
        "fruits": ["Apple", "Banana", "Cherry"],
    }
    return HttpResponse(template.render(context, request))
