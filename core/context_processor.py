from .models import *
from settings.models import *
from page.models import Page
from attraction.models import Attraction
from ota.models import *
from core.models import *
# from payment.models import *

def default(request):
    favicon = Favicon.objects.first()
    logo = Logo.objects.first()
    site_info = SiteInfo.objects.first()
    social_links = SocialLinks.objects.first()
    attractions = Attraction.objects.all().order_by('ordering')
    # page_banner = PageBanner.objects.first()
    pages=Page.objects.all()
    otas=OTA.objects.all()
    rooms=Room.objects.all()

   
    return {
        'favicon': favicon,
        'logo': logo,
        'site_info': site_info,
        'social_links': social_links,
        # 'page_banner': page_banner,
        'pages': pages,
        'otas':otas,
        'attractions': attractions,
        'rooms': rooms,
       
       
    }
