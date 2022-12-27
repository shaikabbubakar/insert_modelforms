from django.contrib import admin

# Register your models here.
from app.models import *
class WebpageCustomView(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_per_page=2
    search_fields=['name']
    list_filter=['name','topic_name']

class AccessCustomView(admin.ModelAdmin):
    list_display=['name','date']
    list_display_links=['name','date']
    search_fields=['name']
    list_filter=['name','date']

admin.site.register(Topic)
admin.site.register(webpage,WebpageCustomView)
admin.site.register(Access_records,AccessCustomView)