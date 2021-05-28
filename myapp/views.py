from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from datetime import datetime
from myapp.models import member,NewsUnit,Order,Orderview
from myapp import form, models
import math,json,random,string
from django.template import RequestContext
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from django.contrib.auth.hashers import make_password, check_password
import json


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
            datas = json.loads(request.POST.get("data"))

            for data in datas:
                unit = Order.objects.create(customname=name, customaccount=account, unitname=data[1],
                                            unitnum=data[2], unitprice=data[3], nowtime=now)
                unit.save()
                orderview = Orderview.objects.get(id=data[0])
                orderview.delete()

            result = 'true'


    return HttpResponse(json.dumps({"result": result}))

def inserorderview(request):

    if 'account' in request.session:
        if request.method == "POST":
            account = request.session['account']
            name = member.objects.get(account=account).Name
            datas = json.loads(request.POST.get("data"))

            for data in datas:
                result = 'true'
                if data:
                    try:
                        unit = Orderview.objects.get(customaccount=account, salename=data[0])
                        unit.salenum = int(unit.salenum) + int(data[1])
                        unit.saleprice = int(unit.saleprice) + int(data[2])
                    except Orderview.DoesNotExist:

                        unit = Orderview.objects.create(customname=name, customaccount=account,
                                                        salename=data[0], salenum=data[1],
                                                        saleprice=data[2])

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
    pigs = models.pigview.objects.all()
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
    beefs=models.beefview.objects.all()
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
    chickens = models.chickenview.objects.all()
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
    lambs=models.lambview.objects.all()
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
    seafoods=models.seafoodview.objects.all()
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
    agaricuses=models.agaricusview.objects.all()
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
    vegetables=models.vegetableview.objects.all()
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


class sic:
    s_str=0
    Name =""
    account=""
    password=""
    email=""
    date=""
    phone=""
    address=""
    str=""

def signup(request):
    if 'account' in request.session:
        log='login'
    if request.method =="POST":
            upform = form.signupform(request.POST)
            if upform:
                if upform.is_valid():
                    sic.Name = upform.cleaned_data['Name']
                    sic.account = upform.cleaned_data['account']
                    sic.password = upform.cleaned_data['password']
                    sic.email = upform.cleaned_data['email']
                    sic.date = upform.cleaned_data['date']
                    sic.phone = upform.cleaned_data['phone']
                    sic.address = upform.cleaned_data['address']
                    try:
                        models.member.objects.get(email=sic.email)
                        em_error = "該信箱被註冊過"
                        try:
                            models.member.objects.get(account=sic.account)
                            ac_error = "該用戶被註冊過"
                        except:
                            ac_error=""
                    except member.DoesNotExist:
                        try:
                            models.member.objects.get(account=sic.account)
                            ac_error = "該用戶被註冊過"
                        except member.DoesNotExist:
                            sic.s_str = "".join(
                                random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
                                                  , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'
                                                  , 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
                                               '8', '9'
                                                  , 'A', 'B', 'C', 'D', 'E', 'F', 'G'
                                                  , 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'
                                                  , 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 6)).replace(
                                " ", "")

                            strSmtp = "smtp.gmail.com:587"
                            strAccount = "4181062@gmail.com"
                            strPassword = "d1074181062"

                            content = "驗證碼:" + sic.s_str
                            msg = MIMEText(content)

                            msg["Subject"] = "帳號認證"
                            mailto = sic.email

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
                            return redirect('/signup/em_cap')

    else:
        upform = form.signupform()
    return render(request, "signup.html", locals())

def em_cap(request):
    ran= sic.s_str
    message = sic.str
    em=sic.email

    if request.method == "POST":
        if request.POST.get("cap") == ran:
            h_pa = make_password(sic.password, None, 'pbkdf2_sha256')
            unit = member.objects.create(Name=sic.Name, account=sic.account, password=h_pa, email=sic.email,
                                          date=sic.date, phone=sic.phone, address=sic.address)
            unit.save()
            sic.Name = ""
            sic.account = ""
            sic.password = ""
            sic.email = ""
            sic.date = ""
            sic.phone = ""
            sic.address = ""
            sic.s_str=""
            message = sic.str = "成功"
        elif request.POST.get("cls"):
            sic.str = ""
        elif request.POST.get("cap") == "":
            message = sic.str = ""
        elif request.POST.get("cap") != ran:
            message = sic.str = "錯誤"

    return render(request, "em_cap.html", locals())






def login(request):
    if 'account' in request.session:
        log='login'
    if request.method =="POST":
        inform = form.loginform(request.POST)
        if inform.is_valid():
            if not 'account' in request.session:
                account = inform.cleaned_data['account']
                password = inform.cleaned_data['password']
                try:
                    omember=member.objects.get(account=account)
                    if(check_password(password,omember.password)):
                        request.session['account'] = request.POST['account']
                        message = request.session['account'] + "登入成功"
                        log = "login"
                    else:
                        pa_message="密碼錯誤"

                except member.DoesNotExist:
                    message = '該用戶尚未註冊'



    else:

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
            return redirect("/contactus")

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