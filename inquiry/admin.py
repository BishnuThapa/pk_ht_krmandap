from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','message','inquired_at']