from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(Popup)
class PopupAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'created_at', 'updated_at')

    # def has_add_permission(self, request, obj=None):
    #     return False

    def thumbnail(self, object):
        return format_html('<img src="{}" width="120" style="border-radius:5%;" />'.format(object.image.url))
