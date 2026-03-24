from django.db import models

# Create your models here.


class Offer(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='offers',
                              blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'
