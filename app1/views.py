import re
from django.db.models.fields import SlugField
from django.http import request
from django.shortcuts import redirect, render,HttpResponse
from .models import gallery
from .models import page
from hitcount.views import HitCountDetailView
from .models import naac
import os

import string 
import random 
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

    from.models import pop

    f=pop.objects.all()[0]
    p=pop.objects.all().order_by('-id')

    data={
        'gal':gal,
        'news':news,
        'visit':visit,
        'rec':rec,
        'p':p,
        'f':f,
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

def placement2022(request):
    return render(request, "pacement2022.html")

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

    funcap3 = capcode()
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

        hstr = request.POST.get('hstr')
        cap = request.POST.get('cap')

        if str(hstr) == str(cap):
            from .models import registration
    
            fm = registration(name=name, contact=phone, wp=wp, address=address, course=course, is_pcm=ispcm, cast=cast, mission_branch=ibranch, is_loan=loan, is_instalment=insta, other_interasted_branches=oib)

            fm.save()
            return render(request, "succ.html")
        else:
            return HttpResponse("<h1>Invalid Capture Code</H1> <h5>Go Back And Resubmit Form With Correct Capture Code Shown In Box</h5>")
        
    return render(request, "reg.html",{'funcap3':funcap3})

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

def aluminireg(request):
    funcapal = capcode()
    if request.method=="POST":
        
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        
        mobile = request.POST.get('mobile')
        yop = request.POST.get('yop')
        dob = request.POST.get('dob')
        maritalstaus = request.POST.get('maritalstaus')
        profession = request.POST.get('profession')
        add = request.POST.get('add')
        add2 = request.POST.get('add2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        aftergraduation = request.POST.get('aftergraduation')
        memorie = request.POST.get('memorie')
        hstr = request.POST.get('hstr')
        cap = request.POST.get('cap')

        name = fname+" "+lname
        address = add+" "+add2+" "+city+" "+state+" "+zip
   
        strmobile=str(mobile)
        stryop=str(yop)
        strdob=str(dob)
        stremail1=str(email)
        print(email)


        if str(hstr) == str(cap):
        
            from app1.models import alumini

            ob = alumini(name=name, email=stremail1, mobile=strmobile, yop=stryop, dob=strdob, maritalstaus=maritalstaus, profession=profession,address=address,aftergraduation=aftergraduation,memorie=memorie)
            ob.save()

            return render(request, "succ.html")
        else:
             return HttpResponse("<h1>Invalid Capture Code</H1> <h5>Go Back And Resubmit Form With Correct Capture Code Shown In Box</h5>")
        
    return render(request, "naac/aluminireg.html",{'funcapal':funcapal})



def contact_us(request):

    funcap2  = capcode()    
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('sub')
        msg = request.POST.get('msg')
        hstr = request.POST.get('hstr')
        cap = request.POST.get('cap')

        if str(hstr) == str(cap):
        
            from app1.models import contact

            ob = contact(name=name, email=email, subject=subject, msg=msg)
            ob.save()

            return render(request, "succ.html")
        else:
             return HttpResponse("<h1>Invalid Capture Code</H1> <h5>Go Back And Resubmit Form With Correct Capture Code Shown In Box</h5>")
        


    return render(request, "contactus.html",{'funcap2':funcap2})


# 4040

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error_404.html', data)

def capcode():
    N = 5
    res = ''.join(random.choices(string.ascii_uppercase +  string.digits, k = N)) 
    strres = str(res)
    return strres



def feedback(request):
    funcap = capcode()
    if request.method=="POST":
        name = request.POST.get('name')
       # phone = request.POST.get('phone')
        email = request.POST.get('email')
        wfrom = request.POST.get('wfrom')
        cmt = request.POST.get('cmt')

        hstr = request.POST.get('hstr')
        cap = request.POST.get('cap')


        if str(hstr) == str(cap):
            from .models import feedback

            fd = feedback(name=name,email=email,wfrom=wfrom,cmt=cmt)

            fd.save()
            return render(request,'succ.html')
        else:
            return HttpResponse("<h1>Invalid Capture Code</H1> <h5>Go Back And Resubmit Form With Correct Capture Code Shown In Box</h5>")
        

    return render(request,'feedback.html',{'funcap':funcap})

def ilad(request):
    return render(request,'ilad.html')

def ilfy(request):
    return render(request,'ilfy.html')

def ildse(request):

    return render(request,'ildse.html')



