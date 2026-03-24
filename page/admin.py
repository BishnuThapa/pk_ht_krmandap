from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.


class Seo(admin.StackedInline):
    model = Seo
    extra = 1
    max_num=1



@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at']
    prepopulated_fields = {
        'slug': ['title', ]
    }
    inlines = (Seo,)
