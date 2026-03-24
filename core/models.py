from django.db import models
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.conf import settings
import os
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Convert
from django.utils import timezone
# Create your models here.


class Amenities(models.Model):
    ammenity_name = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='amenities')
    description = models.TextField(null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ammenity_name

    class Meta:
        verbose_name = 'Amenities'
        verbose_name_plural = 'Amenities'


class Room(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    image = models.ImageField(
        upload_to='rooms', blank=True, null=True, default="default.jpg")
    original_price_per_night = models.PositiveIntegerField(
        help_text='in USD', blank=True, null=True)
    price_per_night = models.PositiveIntegerField(help_text='in USD')
    no_of_bed = models.CharField(
        max_length=255, blank=True, null=True, help_text='eg. 2 single bed')
    room_size = models.CharField(max_length=255, help_text='172ft square')
    max_guests = models.CharField(max_length=255, help_text='eg. for 2 adults')
    amenities = models.ManyToManyField(Amenities, blank=True, null=True)
    # short_description = models.TextField(null=True, blank=True)
    description = CKEditor5Field(config_name='extends')
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

        # Resized JPEG (fallback)
    image_optimized = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200)],
        format='JPEG',
        options={'quality': 80}
    )

    # WebP optimized version
    image_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200), Convert('WEBP')],
        format='WEBP',
        options={'quality': 80}
    )


class RoomGallery(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='room/gallery')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Room Gallery'
        verbose_name_plural = 'Room Gallery'

       # Resized JPEG (fallback)
    image_optimized = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200)],
        format='JPEG',
        options={'quality': 80}
    )

    # WebP optimized version
    image_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200), Convert('WEBP')],
        format='WEBP',
        options={'quality': 80}
    )
