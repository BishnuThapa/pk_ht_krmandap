from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.


def service(request):
    all_services = Services.objects.all()
    context = {
        'all_services': all_services,
    }
   
    return render(request, 'services.html', context)


def service_detail(request, slug):
    single_service = get_object_or_404(Services, slug=slug)
    all_services = Services.objects.all()  # get all services for sidebar

    context = {
        'single_service': single_service,
        'all_services': all_services,  # pass to template
    }
    return render(request, 'service-detail.html', context)
