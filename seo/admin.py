from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Seo)
class SeoAdmin(admin.ModelAdmin):
    list_display = ['title', 'keywords', 'description']
