from django.contrib import admin
from myfolder.models import Type,Portfolio,Services,Lavozim,Team,Contact,Subscribe
# Register your models here.

class AdminType(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Type,AdminType)



class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','name','tur','rasm','date']
admin.site.register(Portfolio,AdminPortfolio)



class AdminServices(admin.ModelAdmin):
    list_display = ['id','name','rasm','date']
admin.site.register(Services,AdminServices)



class AdminLavozim(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Lavozim,AdminLavozim)



class AdminTeam(admin.ModelAdmin):
    list_display = ['id','name','surname','rasm','lavozim','project_url','comment']
admin.site.register(Team,AdminTeam)




class AdminContact(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Contact,AdminContact)

class AdminSubscribe(admin.ModelAdmin):
    list_display = ['id','gmail']
admin.site.register(Subscribe,AdminSubscribe)