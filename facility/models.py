from django.db import models

# Create your models here.
class Facility(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='facilities',help_text='small png image preferable.', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'