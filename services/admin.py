from django.contrib import admin
from .models import Services
from django.utils.html import format_html
# Register your models here.

# admin.site.register(Services)

@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'ordering',
                    'is_active', 'created_at', 'updated_at')
    list_editable = ('ordering', )
    prepopulated_fields = {
        'slug': ['title', ]
    }

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" style="border-radius:5%;" />',
                obj.image.url
            )
        return "—"
