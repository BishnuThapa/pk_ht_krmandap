from django.urls import path, include
from . import views
from aboutus.views import about
urlpatterns = [
    path('', views.index, name="index"),
    path('about-us', about, name="about"),
    path('special-offer', views.offer, name="offer"),
    path('gallery', views.gallery, name="gallery"),
    # path('registration', views.registration, name="registration"),
    path('rooms', views.rooms, name="rooms"),
    path('rooms/<slug:slug>/', views.room_detail, name="room-detail"),
    # path('book-your-stay/', views.room_booking, name="room-booking"),
    # path('booking-success/', views.booking_success, name="booking-success"),
    # path('dining', views.dining, name="dining"),
    path('nearby-attractions', views.attraction, name="attraction"),
    path('contact-us', views.contact, name="contact"),
    path('faqs', views.faqs, name="faq"),
    path('page/', include('page.urls')),
    path('blog/', include('blog.urls')),

]
