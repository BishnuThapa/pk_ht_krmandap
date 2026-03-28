from django.shortcuts import render,get_object_or_404
from gallery.models import Gallery
from faq.models import Faq
from attraction.models import Attraction
from aboutus.models import About
from slider.models import Slider
from offer.models import Offer
from inquiry.models import Inquiry
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    faqs = Faq.objects.all().order_by('ordering')
    about = About.objects.first()
    sliders = Slider.objects.filter(is_active=True).order_by('serial')
    # attractions = Attraction.objects.all().order_by('ordering')
    offers=Offer.objects.filter(is_active=True).order_by('ordering')
    images = Gallery.objects.all().order_by('ordering')
    # room = Room.objects.first()

    context = {
        'faqs': faqs,
       'about': about,
        'sliders': sliders,
        'offers':offers,
        # 'attractions': attractions,
        'images': images,
        # 'room': room,
    }
    return render(request, 'index.html',context)


def attraction(request):
    attractions=Attraction.objects.all().order_by('ordering')
    context={
        'attractions':attractions
        }
    return render(request, 'attraction.html',context)

def gallery(request):
    images=Gallery.objects.all().order_by('ordering')
    context={
        'images':images
        }
    return render(request, 'gallery.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        message = request.POST.get('message')

        # Save to DB
        Inquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            country=country,
            message=message,
        )
        return HttpResponse('<p class="text-success">Your message has been sent successfully!</p>')
    return render(request, 'contact.html')

def faqs(request):
    faqs=Faq.objects.all().order_by('ordering')
    context={
        'faqs':faqs
        }
    return render(request, 'faqs.html',context)


def offer(request):
    offers=Offer.objects.filter(is_active=True).order_by('ordering')
    context={
        'offers':offers
        }
    return render(request, 'offer.html',context)

def rooms(request):
    # rooms=Room.objects.all().order_by('ordering')
    # context={
    #     'rooms':rooms
    #     }
    return render(request, 'rooms.html')

def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    gallery_images = RoomGallery.objects.filter(room=room)
    context = {
        'room': room,
        'gallery_images': gallery_images,
    }
    return render(request, 'room-detail.html', context)

def error_404(request, exception):
    return render(request, '404.html', status=404)
