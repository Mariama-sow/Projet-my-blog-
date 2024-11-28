from django.contrib import admin
from .models import Articles , Comment

class Articlesadmin(admin.ModelAdmin):
    list_display=('title','sumary','date_pub','created_at')
    date_hierarchy = 'date_pub'

admin.site.register(Articles,Articlesadmin)
