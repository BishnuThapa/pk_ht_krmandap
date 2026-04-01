from django.shortcuts import render,get_object_or_404
from gallery.models import Gallery
from faq.models import Faq
from attraction.models import Attraction
from aboutus.models import About
from slider.models import Slider
from offer.models import Offer
from inquiry.models import Inquiry
from django.http import HttpResponse
from facility.models import Facility
from .models import *
from ota.models import OTA
from blog.models import Blog
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from datetime import datetime


# Create your views here.


def index(request):
    faqs = Faq.objects.all().order_by('ordering')
    about = About.objects.first()
    facilities = Facility.objects.all()
    sliders = Slider.objects.filter(is_active=True).order_by('serial')
    attractions = Attraction.objects.all().order_by('ordering')
    offers=Offer.objects.filter(is_active=True).order_by('ordering')
    images = Gallery.objects.all().order_by('ordering')
    room = Room.objects.filter(is_active=True)
    otas=OTA.objects.filter(is_active=True).order_by('ordering')
    blogs=Blog.objects.filter(is_active=True).order_by('-created_at')[:4]

    context = {
        'faqs': faqs,
       'about': about,
        'facilities': facilities,
        'sliders': sliders,
        'offers':offers,
        'attractions': attractions,
        'images': images,
        'room': room,
        'otas': otas,
        'blogs': blogs,
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
    rooms=Room.objects.all()
    context={
        'rooms':rooms
        }
    return render(request, 'rooms.html',context)

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



def room_booking(request):
    rooms = Room.objects.all()
    if request.method == 'GET':
        id = request.GET.get('id')
        room = request.GET.get('room')
        price_per_night = request.GET.get('price_per_night')
        
    if request.method == "POST":
        room_id = request.POST.get('room')
        no_of_rooms = request.POST.get('no_of_rooms')
        adults = request.POST.get('adults')
        check_in_date = request.POST.get('checkin')
        check_out_date = request.POST.get('checkout')
        guest_name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        special_request=request.POST.get('message')
        total_pricing = request.POST.get('pricing')

        room = get_object_or_404(Room, id=room_id)
        # check_in_date = datetime.strptime(check_in_date, '%d/%m/%Y').date()
        # check_out_date = datetime.strptime(check_out_date, '%d/%m/%Y').date()

        check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d').date()
        # print(name, email, phone, subject, message)
        booking=Booking(room=room, no_of_rooms=no_of_rooms, adults=adults, check_in_date=check_in_date, check_out_date=check_out_date,
                               guest_name=guest_name, phone=phone, email=email, special_request=special_request,total_pricing=total_pricing)
        booking.save()
        # Retrieve the booking_id
        booking_id = booking.booking_id
        # messages.success(request, 'Your message sent successfully!')
        subject = "Booking Confirmation"
        # message = "Room Booking" + " " + "email " + " " + email + " " + "phone " + phone
        from_email = 'Buki Lazimpat - Boutique Hotel <admin@bukihotels.com>'
        recipient_list = ['website@bukihotels.com',email]
        # Render the HTML template with booking details
        html_content = render_to_string('booking-confirmation.html', {
            
            'guest_name': guest_name,
            'email': email,
            'phone': phone,
            'check_in_date': check_in_date,
            'check_out_date': check_out_date,
            'adults': adults,
            'room': room.title,
            'special_request':special_request,
            'total_nights': (check_out_date - check_in_date).days,
            'total_pricing': total_pricing,
            'booking_id': booking_id  # Pass the booking_id to the context

        })
        # Create plain text for email clients that do not support HTML
        text_content = strip_tags(html_content)
        # send_mail(subject, message, from_email, recipient_list)
        # Send the email with HTML content
        email_message = EmailMultiAlternatives(
            subject, text_content, from_email, recipient_list)
        email_message.attach_alternative(html_content, "text/html")
        email_message.send()
        context={
            'guest_name': guest_name,
            'email': email,
            'phone': phone,
            'check_in_date': check_in_date,
            'check_out_date': check_out_date,
            'adults': adults,
            'room': room.title,
            'special_request': special_request,
            'total_nights': (check_out_date - check_in_date).days,
            'total_pricing': total_pricing,
            'booking_id': booking_id  # Pass the booking_id to the context
        }
        # return redirect('index')
        return render(request,'booking-confirmation.html',context)
    context = {
        'id':id,
        'room':room,
        'rooms': rooms,
        'price_per_night': price_per_night
    }
    return render(request, 'room-booking.html',context)