from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def about(request):

    about = About.objects.first()
    context = {
        'about': about,

    }
    return render(request, 'about.html', context)


def chairmanmessage(request):
    chairman_message = ChairmanMessage.objects.first()
    context = {
        'chairman_message': chairman_message,

    }
    return render(request, 'md-message.html', context)

def vision(request):

    vision = Vision.objects.first()
    context = {
        'vision': vision,

    }
    return render(request, 'vision.html', context)


def goal(request):

    goal = Goals.objects.first()
    context = {
        'goal': goal,

    }
    return render(request, 'goal.html', context)


def whyus(request):

    whyus = WhyUs.objects.first()
    context = {
        'whyus': whyus,

    }
    return render(request, 'why-us.html', context)


def profile(request):

    profile = CompanyProfile.objects.first()
    context = {
        'profile': profile,

    }
    return render(request, 'company-profile.html', context)

def certification(request):

    certifications = LegalDocument.objects.all()
    context = {
        'certifications': certifications,

    }
    return render(request, 'certification.html', context)
