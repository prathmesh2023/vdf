from django.db.models.fields import SlugField
from django.http import request
from django.shortcuts import render,HttpResponse
from .models import gallery
from .models import page
from hitcount.views import HitCountDetailView
from .models import naac
import os
# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def home(request):
    from .models import gallery,news,viewer
    gal = gallery.objects.all().order_by('-id')[:6]
    news = news.objects.all().order_by('-id')[:6]
    ip = get_client_ip(request)

    if viewer.objects.filter(ip=ip).exists():
        pass

    else:
        viewer = viewer(ip=ip)

        viewer.save()

    from .models import viewer
    visit = viewer.objects.all().count()


    print("ip"+ip)
    from .models import recruter
    rec = recruter.objects.all().order_by('-id')
    data={
        'gal':gal,
        'news':news,
        'visit':visit,
        'rec':rec,
    }
    # return HttpResponse("wellcome")
    return render(request, "home.html", data)


class PostCountHitDetailView(HitCountDetailView):
    model = home        # your model goes here
    template_name= "base.html"
    # slug_field="slug"
    count_hit = True    # set to True if you want it to try and count

def pmassage(request):

    # return HttpResponse("wellcome")
    return render(request, "pmessage.html")


def aplied_science(request):

    return render(request, "dep/as.html")

def gallery(request):
    from .models import gallery
    gal = gallery.objects.all().order_by('-id')
    data={'gal':gal}

    return render(request, "gallery.html",data)


def pages(request, link):
    link = page.objects.filter(link=link)
    return render(request, "page.html", {'link':link[0]})


def trainningap(request):

    return render(request, "trainning.html")


def placement2021(request):

    return render(request, "place.html")

def library(request):

    return render(request, "library.html")


def workshop(request):

    return render(request, "workshop.html")


def news(request,link):
    from .models import news 

    link = news.objects.filter(link=link)
    news = news.objects.all().order_by('-id')

    return render(request, "news.html",{'link':link[0],'news':news})

def registration(request):


    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        wp = request.POST.get('wp')
        address = request.POST.get('add')
        course = request.POST.get('course')
        ispcm = request.POST.get("ispcm")
        cast = request.POST.get("cast")
        ibranch = request.POST.get("branch")
        loan = request.POST.get("loan")
        insta =request.POST.get("insta")

        oib=request.POST.getlist('oib')

  
        from .models import registration
 
        fm = registration(name=name, contact=phone, wp=wp, address=address, course=course, is_pcm=ispcm, cast=cast, mission_branch=ibranch, is_loan=loan, is_instalment=insta, other_interasted_branches=oib)

        fm.save()

        return render(request, "reg.html")
pass


# about 

def mou(request,link):

    from .models import mou

    link = mou.objects.filter(link=link)

    return render(request, "mou.html",{'link':link[0]})

def aboutvdf(request):

    return render(request, "about/about.html")

def mous(request):
    from .models import mou

    mou = mou.objects.all()

    return render(request, "mous.html",{'mou':mou})


def our_inspiration(request):

    return render(request, "about/ourinsp.html")

def primassage(request):

    return render(request, "about/principal.html")







# dep

def about_as(request):

    return render(request, "dep/as/asc.html")


def ce(request):

    return render(request, "dep/ce/acs.html")

def co(request):

    return render(request, "dep/co/co.html")

def el(request):

    return render(request, "dep/el/el.html")

def et(request):

    return render(request, "dep/et/et.html")

def me(request):

    return render(request, "dep/me/me.html")


# faculties:



def facce(request):

    return render(request, "dep/ce/fac.html")

def facco(request):

    return render(request, "dep/co/fac.html")

def facel(request):

    return render(request, "dep/el/fac.html")

def facet(request):

    return render(request, "dep/et/fac.html")

def facme(request):

    return render(request, "dep/me/fac.html")

def facas(request):

    return render(request, "dep/as/fac.html")


# naac


def aqar2019_2020(request):

    return render(request, "naac/aqar1920-2020.html")

def aqar2020_2021(request):

    return render(request, "naac/aqar2020-2021.html")

def mnaac(request):
    
    from .models import naac
    
    naac = naac.objects.all()
    
    data = {
        'naac':naac,
    }

    return render(request, "naac/mnaac.html",data)


# 4040

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error_404.html', data)




