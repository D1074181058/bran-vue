"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from myapp import views


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^dish/pig/$',views.pig),
    url(r'^dish/beef/$',views.beef),
    url(r'^dish/chicken/$',views.chicken),
    url(r'^dish/lamb/$',views.lamb),
    url(r'^dish/seafood/$',views.seafood),
    url(r'^dish/agaricus/$',views.agarigus),
    url(r'^dish/vegetables/$',views.vegetables),

    url(r'^newinfo/',views.newinfo),
    url(r'^newinfoindex/(\d+)/$',views.newinfo),
    url(r'^infodetail/(\d+)/$',views.infodetail),

    url(r'^contactus/',views.contactus),

    url(r'^aboutus/',views.aboutus),




    url(r'^signup/$',views.signup),
    url(r'^signup/em_cap/$',views.em_cap),

    url(r'^login/',views.login),

    url(r'^captcha/',include('captcha.urls')),

    url(r'^logout/',views.logout),

    url(r'^hlogout/',views.hlogout),


    url(r'^backview/',views.backview),
    url(r'^sal_view/',views.sal_view),
    url(r'^inserorder/', views.inserorder),
    url(r'^inserorderview/', views.inserorderview),
    url(r'^delorder/', views.delorder),
    url(r'^delorderview/', views.delorderview),



    url(r'^0/',views.test),

    #url(r'^login1/$',views.login1),
    #url(r'^login2/$',views.login2),
    #url(r'^hello/(\w+)/',hello),



]
