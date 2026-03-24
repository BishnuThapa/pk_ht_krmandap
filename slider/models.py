from django.db import models


class Slider(models.Model):
    image = models.ImageField(upload_to='slider',
                              help_text='1920*1280 px')
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.TextField(null=True, blank=True)
    serial = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'
