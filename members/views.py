from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def testPage(request) :
    return HttpResponse("Test page for Django On The Water App")
