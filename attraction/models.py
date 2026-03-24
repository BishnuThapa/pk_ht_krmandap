from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.conf import settings
import os
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Convert
# Create your models here.


class Attraction(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='attraction',
                              blank=True, null=True, help_text="306*323")
    distance= models.CharField(max_length=255,blank=True, null=True,help_text="eg. 2 km")
    description = CKEditor5Field(config_name='extends')
    ordering = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Attraction'
        verbose_name_plural = 'Attractions'
