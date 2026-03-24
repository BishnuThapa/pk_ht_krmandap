from django.db import models

# Create your models here.


class Faq(models.Model):
    question = models.CharField(max_length=255, null=True, blank=True)
    answer = models.TextField()
    ordering = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
