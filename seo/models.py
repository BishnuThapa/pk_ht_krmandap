from django.db import models

# Create your models here.


class Seo(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'
