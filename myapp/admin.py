from django.contrib import admin
from myapp.models  import member,NewsUnit,Order,Orderview,beefview,chickenview,pigview,lambview,agaricusview,seafoodview,vegetableview


# Register your models here.
class memberAdmin(admin.ModelAdmin):
     list_display=('id','Name', 'account', 'password', 'email','date', 'phone', 'address')
     ordering = ('id',)
admin.site.register(member,memberAdmin)

class NewsUnitAdmin(admin.ModelAdmin):
     list_display=('id','catego', 'nickname', 'title', 'message', 'pubtime','enabled','press')
     ordering = ('id',)
admin.site.register(NewsUnit,NewsUnitAdmin)

class OrderAdmin(admin.ModelAdmin):
     list_display=('customname','customaccount','customemail', 'customphone', 'customaddress', 'unitname','unitnum','unitprice','nowtime')
     ordering = ('id',)
admin.site.register(Order,OrderAdmin)

class OrderviewAdmin(admin.ModelAdmin):
     list_display=('customname','customaccount', 'salename','salenum','saleprice')
     ordering = ('id',)
admin.site.register(Orderview,OrderviewAdmin)






class beefviewAdmin(admin.ModelAdmin):
     list_display=('id','salename','saleprice','imgname')
     ordering = ('id',)
admin.site.register(beefview,beefviewAdmin)

class pigviewAdmin(admin.ModelAdmin):
     list_display=('id','salename','saleprice','imgname')
     ordering = ('id',)
admin.site.register(pigview,pigviewAdmin)

class chickenviewAdmin(admin.ModelAdmin):
     list_display=('id','salename','saleprice','imgname')
     ordering = ('id',)
admin.site.register(chickenview,chickenviewAdmin)

class lambviewAdmin(admin.ModelAdmin):
     list_display=('id','salename','saleprice','imgname')
     ordering = ('id',)
admin.site.register(lambview,lambviewAdmin)

class agaricusviewAdmin(admin.ModelAdmin):
     list_display=('id','salename','saleprice','imgname')
     ordering = ('id',)
admin.site.register(agaricusview,agaricusviewAdmin)

class seafoodviewAdmin(admin.ModelAdmin):
     list_display=('id','salename','saleprice','imgname')
     ordering = ('id',)
admin.site.register(seafoodview,seafoodviewAdmin)

class vegetableviewAdmin(admin.ModelAdmin):
     list_display=('id','salename','saleprice','imgname')
     ordering = ('id',)
admin.site.register(vegetableview,vegetableviewAdmin)