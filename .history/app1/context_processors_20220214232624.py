from .models import naac
# for base template

def show_naac(request):
    
    return {'show_naac':naac.objects.all()}
