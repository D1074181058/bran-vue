from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def sayhello(request):
    return HttpResponse("Django")

def hello(request):
    now=datetime.now()
    return render(request,"hello.html",locals())
def pig(request):
    now=datetime.now()
    return render(request,"pig.html",locals())
def beef(request):
    now=datetime.now()
    return render(request,"beef.html",locals())
def chicken(request):
    now=datetime.now()
    return render(request,"chicken.html",locals())
def lamb(request):
    now=datetime.now()
    return render(request,"lamb.html",locals())
def seafood(request):
    now=datetime.now()
    return render(request,"seafood.html",locals())
def agarigus(request):
    now=datetime.now()
    return render(request,"agaricus.html",locals())
def vegetables(request):
    now=datetime.now()
    return render(request,"vegetables.html",locals())


def test(request):
    now=datetime.now()
    return render(request,"test.html",locals())