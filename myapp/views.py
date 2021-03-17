from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from myapp.models import member


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
def login(request):
    if request.method =="POST":
        Name=request.POST['Name']
        account = request.POST['account']
        password = request.POST['password']
        unit = member.objects.create(Name=Name,account=account,password=password)
        unit.save()
        return redirect('/')
    else:
        massage='輸入'
    return render(request, "login.html", locals())


def test(request):
    now=datetime.now()
    return render(request,"test.html",locals())