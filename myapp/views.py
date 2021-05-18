from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from datetime import datetime
from myapp.models import member,NewsUnit,Order,Orderview
from myapp import form
import math,json
from django.template import RequestContext
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from django.contrib.auth.hashers import make_password, check_password



@csrf_exempt
def sayhello(request):
    return HttpResponse("Django")
def test(request):
    now=datetime.now()
    return render(request,"test.html",locals())

def backview(request):
    i=0
    lis=[]
    orderall = Order.objects.all()
    for order in orderall:
        i+=1
        lis.append(i)
    now = datetime.now()
    return render(request, "backview.html", locals())
def sal_view(request):
    if 'account' in request.session:
        log='login'
        account = request.session['account']
        message = account + "已登入"
        orderviewall = Orderview.objects.filter(customaccount=account)
    now = datetime.now()
    return render(request, "sal_view.html", locals())


def inserorder(request):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if 'account' in request.session:
        if request.method == "POST":
            account = request.session['account']
            name = member.objects.get(account=account).Name
            unitname = request.POST.get("unitname")
            unitnum = request.POST.get("unitnum")
            unitprice = request.POST.get("unitprice")
            unit = Order.objects.create(customname=name,customaccount=account,unitname=unitname, unitnum=unitnum, unitprice=unitprice,nowtime=now)
            unit.save()
            ID = request.POST.get("view_id")
            orderview_all = Orderview.objects.get(id=ID)
            orderview_all.delete()
    return render(request,"home.html", locals())

def inserorderview(request):
    if 'account' in request.session:
        result = "True"
        if request.method == "POST":
            account = request.session['account']
            name = member.objects.get(account=account).Name
            unitname = request.POST.get("unitname")
            unitnum = request.POST.get("unitnum")
            unitprice = request.POST.get("unitprice")
            try:
                unit=Orderview.objects.get(customaccount=account,salename=unitname)
                unit.salenum = int(unit.salenum)+int(unitnum)
                unit.saleprice = int(unit.saleprice)+int(unitprice)
            except Orderview.DoesNotExist:
                unit = Orderview.objects.create(customname=name,customaccount=account,salename=unitname, salenum=unitnum, saleprice=unitprice)
            unit.save()
    else:
        result = "Error"
    return HttpResponse(json.dumps({"result": result}))

def delorderview(request):
    if request.method == "POST":
        ID=request.POST.get("view_id")
        orderview=Orderview.objects.get(id=ID)
        orderview.delete()
    return render(request, "home.html", locals())


def delorder(request):
    now = datetime.now()
    if request.method == "POST":
        unitname = request.POST.get("unitname")
        unitnum = request.POST.get("unitnum")
        name=request.POST.get("customname")
        nowtime = request.POST.get("nowtime")
        order=Order.objects.get(customname=name,unitname=unitname,unitnum=unitnum,nowtime=nowtime)
        order.delete()
    return render(request, "home.html", locals())

def home(request):
    if 'account' in request.session:
        log = 'login'
        account = request.session['account']
        message = request.session['account']+"已登入"
    now=datetime.now()
    return render(request,"home.html",locals())
def pig(request):
    if 'account' in request.session:
        log = 'login'
        account = request.session['account']
        try:
            orderview = Orderview.objects.filter(customaccount=account)
            viewlen = len(orderview)
        except Orderview.DoesNotExist:
            viewlen = ""
        message = request.session['account']+"已登入"

    now=datetime.now()
    return render(request,"pig.html",locals())

def beef(request):
    if 'account' in request.session:
        log = 'login'
        account = request.session['account']
        try:
            orderview = Orderview.objects.filter(customaccount=account)
            viewlen = len(orderview)
        except Orderview.DoesNotExist:
            viewlen=""
        message = request.session['account'] + "已登入"
    else:
        log ='out'




    now=datetime.now()
    return render(request,"beef.html",locals())
def chicken(request):
    if 'account' in request.session:
        log = 'login'
        account = request.session['account']
        try:
            orderview = Orderview.objects.filter(customaccount=account)
            viewlen = len(orderview)
        except Orderview.DoesNotExist:
            viewlen = ""
        message = request.session['account']+"已登入"

    now=datetime.now()
    return render(request,"chicken.html",locals())
def lamb(request):
    if 'account' in request.session:
        log = 'login'
        account = request.session['account']
        try:
            orderview = Orderview.objects.filter(customaccount=account)
            viewlen = len(orderview)
        except Orderview.DoesNotExist:
            viewlen = ""
        message = request.session['account']+"已登入"

    now=datetime.now()
    return render(request,"lamb.html",locals())
def seafood(request):
    if 'account' in request.session:
        log = 'login'
        account = request.session['account']
        try:
            orderview = Orderview.objects.filter(customaccount=account)
            viewlen = len(orderview)
        except Orderview.DoesNotExist:
            viewlen = ""
        message = request.session['account']+"已登入"

    now=datetime.now()
    return render(request,"seafood.html",locals())
def agarigus(request):
    if 'account' in request.session:
        log = 'login'
        account = request.session['account']
        try:
            orderview = Orderview.objects.filter(customaccount=account)
            viewlen = len(orderview)
        except Orderview.DoesNotExist:
            viewlen = ""
        message = request.session['account']+"已登入"

    now=datetime.now()
    return render(request,"agaricus.html",locals())
def vegetables(request):
    if 'account' in request.session:
        log = 'login'
        account = request.session['account']
        try:
            orderview = Orderview.objects.filter(customaccount=account)
            viewlen = len(orderview)
        except Orderview.DoesNotExist:
            viewlen = ""
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
            h_pa=make_password(password, None, 'pbkdf2_sha256')
            unit = member.objects.create(Name=Name,account=account,password=h_pa,email=email,
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
                    if(member.objects.get(account=account)):
                        if(check_password(password,member.objects.get(account=account).password)):
                            request.session['account'] = request.POST['account']
                            message = request.session['account'] + "登入成功"
                            log = "login"
                        else:
                            message="密碼錯誤"
                    else:
                        message="帳號錯誤"
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
    if 'account' in request.session:
            log='out'
            massage=request.session['account']
            del request.session['account']
    return render(request, "logout.html", locals())

def hlogout(request):

    if 'account' in request.session:
        message=request.session['account']+"已登出"
        del request.session['account']


    return render(request, "login.html", locals())


page1 = 1
def newinfo(request,pageindex=None):
    if 'account' in request.session:
        log = 'login'
        account = request.session['account']
        message = request.session['account']+"已登入"
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
    if 'account' in request.session:
        log = 'login'
        account = request.session['account']
        message = request.session['account']+"已登入"
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



def contactus(request):
    if 'account' in request.session:
        log = 'login'
        account = request.session['account']
        message = request.session['account']+"已登入"
    if request.method =="POST":
        contactform=form.contactusform(request.POST)
        if contactform.is_valid():
            Name  = contactform.cleaned_data['Name']
            phone = contactform.cleaned_data['phone']
            title = contactform.cleaned_data['title']
            content = contactform.cleaned_data['content']

            strSmtp = "smtp.gmail.com:587"
            strAccount = ""
            strPassword = ""

            content = "建議人姓名 : " + Name + "\n"+"建議人電話 : " + phone + "\n"+"建議內容   :\n" + content + "\n"
            msg = MIMEText(content)

            msg["Subject"] = title
            mailto = ""

            server = SMTP(strSmtp)
            server.ehlo()
            server.starttls()
            try:
                server.login(strAccount, strPassword)
                server.sendmail(strAccount, mailto, msg.as_string())
                hint = "郵件已發送！"
            except SMTPAuthenticationError:
                hint = "無法登入！"
            except:
                hint = "郵件發送產生錯誤！"
            server.quit()

        else:
            message='有欄位錯誤'
    else:
        contactform = form.contactusform()
    return render(request , "contactus.html",locals())
def aboutus(request):
    if 'account' in request.session:
        log = 'login'
        message = request.session['account']+"已登入"
    now=datetime.now()
    return render(request,"aboutus.html",locals())