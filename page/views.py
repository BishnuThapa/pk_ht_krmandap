from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.


def page(request, slug):
    # banner=Banner.objects.first()
    seo=Seo.objects.first()
    page = get_object_or_404(Page, slug=slug)
    context = {
        # 'banner':banner,
        'seo': seo,
        'page': page,
    }

    return render(request, 'page.html',context)