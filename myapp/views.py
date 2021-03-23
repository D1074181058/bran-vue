from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from myapp.models import member
from myapp import form


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
def signup(request):
    if request.method =="POST":
        upform=form.signupform(request.POST)
        if upform.is_valid():
            Name=upform.cleaned_data['Name']
            account = upform.cleaned_data['account']
            password = upform.cleaned_data['password']
            email = upform.cleaned_data['email']
            date = upform.cleaned_data['date']
            phone = upform.cleaned_data['phone']
            address = upform.cleaned_data['address']
            unit = member.objects.create(Name=Name,account=account,password=password,email=email,date=date,phone=phone,address=address)
            unit.save()
            return redirect('/')
        else:
            message='有欄位錯誤'
    else:

        upform = form.signupform()

    return render(request, "signup.html", locals())
def login(request):
    if request.method =="POST":
        account = request.POST['account']
        password = request.POST['password']
        try:
            unit = member.objects.get(account=account,password=password)
        except member.DoesNotExist:
            unit =None

        if unit != None:
            message='登入成功'
            return redirect('/')
        else:
            message='123'
    else:
        message='輸入'
    return render(request, "login.html", locals())


def test(request):
    now=datetime.now()
    return render(request,"test.html",locals())