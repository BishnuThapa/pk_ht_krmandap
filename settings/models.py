from django.db import models

# Create your models here.


class Favicon(models.Model):
    name = models.CharField(max_length=255)
    favicon = models.ImageField(
        upload_to='images', default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Favicon'
        verbose_name_plural = 'Favicon'


class Logo(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(
        upload_to='images', default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo'


class PageBanner(models.Model):
        title = models.CharField(max_length=255)
        image = models.ImageField(upload_to='blogs/banner', default='')
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        def __str__(self):
            return self.title

        class Meta:
            verbose_name = 'Page Banner'
            verbose_name_plural = 'Page Banner'

class SiteInfo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    secondary_email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=100)
    short_description = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Office Information'
        verbose_name_plural = 'Office Information'


class SocialLinks(models.Model):
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    tiktok_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Social Links"

    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'


