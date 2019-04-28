from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
import urllib.request
import urllib.parse
import json

# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def art(request):
    template = loader.get_template('art.html')
    context = {}
    return HttpResponse(template.render(context, request))

def music(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def film(request):
   template = loader.get_template('home.html')
   context = {}
   return HttpResponse(template.render(context, request))
