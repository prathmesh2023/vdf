from django.conf import settings
from app1.models import naac
# for base template

def show_naac(request):
    from .models import naac
    
    return {'show_naac':naac.objects.all()}
