from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(About)
admin.site.register(ChairmanMessage)
admin.site.register(Goals)
admin.site.register(Vision)
admin.site.register(WhyUs)
admin.site.register(CompanyProfile)
admin.site.register(RecruitmentProcess)


@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at','updated_at']