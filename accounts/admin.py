from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account

# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ('groups', 'user_permissions')
    list_filter = ('is_admin', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name',
         'last_name', 'username', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_admin', 'is_superadmin', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def get_readonly_fields(self, request, obj=None):
        # Ensure password is hashed and readonly
        readonly_fields = list(super().get_readonly_fields(request, obj))
        if obj:
            readonly_fields.append('password')
        return readonly_fields

    def save_model(self, request, obj, form, change):
        """
        Hashes the password if it is being set or changed in the admin interface.
        """
        if form.cleaned_data.get('password'):
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)
