from django.contrib import admin
from kombu.transport.django import models as kombu_models
from tuanapp import models
from django.contrib.auth.models import User

class Tuan_admin(admin.ModelAdmin):
	list_display = ('rest_name','min_num','max_num','init','date','crt_num','progress')
	list_filter = ('rest_name','min_num','max_num','init','date','crt_num','progress')
	search_fields = ('rest_name','min_num','max_num','init','date','crt_num','progress')

class Person_admin(admin.ModelAdmin):
	list_display = ('user__username','email')
	list_filter = ('user__username','email',)
	search_fields = ('user__username','email')

admin.site.register(models.Tuan,Tuan_admin)
admin.site.register(models.Person)
admin.site.register(kombu_models.Message)
