from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# from ckeditor.fields import RichTextField
# Create your models here.


class ChairmanMessage(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    featured_image = models.ImageField(
        upload_to='principal', blank=True, null=True, default='')
    description = CKEditor5Field(config_name='extends')

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Message From Chairman'
        verbose_name_plural = 'Message From Chairman'


class About(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    featured_image = models.ImageField(
        upload_to='about', blank=True, null=True, default='')
    description = CKEditor5Field(config_name='extends')

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class WhyUs(models.Model):
    heading = models.CharField(max_length=255)
    image_icon = models.ImageField(
        upload_to='about', blank=True, null=True, default='')
    featured_image = models.ImageField(
        upload_to='about', blank=True, null=True, default='')
    experience=models.IntegerField(default=0)
    short_description = models.TextField()
    description = CKEditor5Field(config_name='extends')

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Why us'
        verbose_name_plural = 'Why us'


class Vision(models.Model):
    heading = models.CharField(max_length=255)
    featured_image = models.ImageField(
        upload_to='image', blank=True, null=True, default='')
    description = CKEditor5Field(config_name='extends')
    

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Vision & Mission'
        verbose_name_plural = 'Vision & Mission'


class Goals(models.Model):
    heading = models.CharField(max_length=255)
    featured_image = models.ImageField(
        upload_to='image', blank=True, null=True, default='')
    description = CKEditor5Field(config_name='extends')
    

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Goals & Core Values'
        verbose_name_plural = 'Goals & Core Values'


class CompanyProfile(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Company Profile'
        verbose_name_plural = 'Company Profile'

# Create your models here.


class RecruitmentProcess(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='recruitment')
    is_active = models.BooleanField(default=True)
    # ordering = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Recruitment Process FLow'
        verbose_name_plural = 'Recruitment Process FLow'

class LegalDocument(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='activities')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Legal Document'
        verbose_name_plural = 'Legal Documents'
