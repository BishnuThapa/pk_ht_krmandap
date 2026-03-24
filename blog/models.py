from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.conf import settings
import os
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Convert
# from filer.fields.image import FilerImageField

    

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='blog')

    description = CKEditor5Field(config_name='extends')
    readtime = models.CharField(
        max_length=10, help_text='eg: 5 min', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blogs'

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


class Seo(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'