from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import GEResults

def results(request):
    election_results = GEResults.objects.all().values()
    template = loader.get_template('results.html')
    context = {'election_results': election_results}
    return HttpResponse(template.render(context, request))

# Create your views here.
