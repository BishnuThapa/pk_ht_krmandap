from django.contrib import admin
from .models import Amenities, Room,RoomGallery,Booking
from django.contrib.admin import ModelAdmin, StackedInline
# Register your models here.
from django.forms import CheckboxSelectMultiple
from django.utils.html import format_html
from django.db import models

class RoomGallery(StackedInline):
    model = RoomGallery
    extra = 1
    max_num = 5


@admin.register(Amenities)
class AmenityAdmin(ModelAdmin):
    list_display = ('ammenity_name',
                    'created_at', 'updated_at')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'original_price_per_night', 'price_per_night',
                    'max_guests', 'is_active')
    list_editable = ('original_price_per_night', 'price_per_night',
                     'max_guests',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = (RoomGallery,)

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" style="border-radius:5%;" />',
                obj.image.url
            )
        return "—"


@admin.register(Booking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'guest_name', 'adults', 'check_in_date',
                    'check_out_date', 'booked_at')
