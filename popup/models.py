from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Popup(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(
        upload_to='images', default='', blank=True, null=True, validators=[FileExtensionValidator(['png', 'jpeg', 'jpg', 'svg'])])
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Popup'
        verbose_name_plural = 'Popup'
