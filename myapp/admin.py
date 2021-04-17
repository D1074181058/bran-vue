from django.contrib import admin
from myapp.models  import member,NewsUnit


# Register your models here.
class memberAdmin(admin.ModelAdmin):
     list_display=('id','Name', 'account', 'password', 'email','date', 'phone', 'address')
     ordering = ('id',)
admin.site.register(member,memberAdmin)

class NewsUnitAdmin(admin.ModelAdmin):
     list_display=('id','catego', 'nickname', 'title', 'message', 'pubtime','enabled','press')
     ordering = ('id',)
admin.site.register(NewsUnit,NewsUnitAdmin)

