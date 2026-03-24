from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.


class SeoInline(admin.TabularInline):
    model = Seo
    extra = 1
    max_num=1

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'thumbnail', 'created_at', 'updated_at']
   
    prepopulated_fields = {
        'slug': ['title', ]
    }
    inlines = (SeoInline,)

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" style="border-radius:5%;" />',
                obj.image.url
            )
        return "—"
