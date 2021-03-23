from django.contrib import admin
from myapp.models  import member


# Register your models here.
class memberAdmin(admin.ModelAdmin):
     list_display=('id','Name', 'account', 'password', 'email','date', 'phone', 'address')
     ordering = ('id',)
admin.site.register(member,memberAdmin)



