from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from datetime import datetime
from myapp.models import member,NewsUnit
from myapp import form
import math
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def sayhello(request):
    return HttpResponse("Django")
def test(request):
    now=datetime.now()
    return render(request,"test.html",locals())


def home(request):
    if 'account' in request.session:
        log = 'login'
        message = request.session['account']+"已登入"

    now=datetime.now()
    return render(request,"home.html",locals())
def pig(request):
    if 'account' in request.session:
        log = 'login'
        message = request.session['account']+"已登入"
    now=datetime.now()
    return render(request,"pig.html",locals())
def beef(request):
    if 'account' in request.session:
        log = 'login'
        message = request.session['account']+"已登入"
    now=datetime.now()
    return render(request,"beef.html",locals())
def chicken(request):
    if 'account' in request.session:
        log = 'login'
        message = request.session['account']+"已登入"
    now=datetime.now()
    return render(request,"chicken.html",locals())
def lamb(request):
    if 'account' in request.session:
        log = 'login'
        message = request.session['account']+"已登入"
    now=datetime.now()
    return render(request,"lamb.html",locals())
def seafood(request):
    if 'account' in request.session:
        log = 'login'
        message = request.session['account']+"已登入"
    now=datetime.now()
    return render(request,"seafood.html",locals())
def agarigus(request):
    if 'account' in request.session:
        log = 'login'
        message = request.session['account']+"已登入"
    now=datetime.now()
    return render(request,"agaricus.html",locals())
def vegetables(request):
    if 'account' in request.session:
        log = 'login'
        message = request.session['account']+"已登入"
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
            unit = member.objects.create(Name=Name,account=account,password=password,email=email,
                                         date=date,phone=phone,address=address)
            unit.save()
            return redirect('/')
        else:
            message='有欄位錯誤'
    else:
        upform = form.signupform()

    return render(request, "signup.html", locals())

def login(request):
    if request.method =="POST":
        inform = form.loginform(request.POST)
        if inform.is_valid():
            if not 'account' in request.session:
                account = inform.cleaned_data['account']
                password = inform.cleaned_data['password']
                try:
                    unit = member.objects.get(account=account,password=password)
                    request.session['account']=request.POST['account']
                    message = request.session['account'] + "登入成功"
                    log="login"
                except member.DoesNotExist:
                    message = '該用戶尚未註冊'

            else:
                messsage=request.session['account']+"已登入"
        else:
            message='有欄位錯誤'
    else:
        message='輸入'
        inform = form.loginform()
    return render(request, "login.html", locals())

def logout(request):
    inform = form.loginform(request.POST)
    if 'account' in request.session:
        message=request.session['account']+"已登出"
        del request.session['account']
        inform = form.loginform()

    return render(request, "home.html", locals())

def hlogout(request):
    inform = form.loginform(request.POST)
    if 'account' in request.session:
        message=request.session['account']+"已登出"
        del request.session['account']
        inform = form.loginform()

    return render(request, "login.html", locals())


page1 = 1
def newinfo(request,pageindex=None):
    global page1
    pagesize = 8
    newsall = NewsUnit.objects.all().order_by('-id')
    datasize = len(newsall)
    totpage = math.ceil(datasize/pagesize)
    if pageindex == None:
        page1 = 1
        newsunits = NewsUnit.objects.filter(enabled=True).order_by('-id')[:pagesize]
    elif pageindex=='1':
        start = (page1-2)*pagesize
        if start >= 0:
            newsunits = NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
            page1 -= 1
    elif pageindex=='2':
        start = page1*pagesize
        if start < datasize:
            newsunits = NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
            page1 += 1
    elif pageindex=='3':
        start = (page1-1)*pagesize
        newsunits = NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
    currentpage = page1
    return render(request, "newinfo.html", locals())

def infodetail(request, detailid=None):
    now = datetime.now()
    newsunits = NewsUnit.objects.get(id=detailid)
    category = newsunits.catego
    title = newsunits.title
    pubtime = newsunits.pubtime
    nickname = newsunits.nickname
    message = newsunits.message
    newsunits.press += 1
    newsunits.save()
    return render(request, "infodetail.html", locals())



