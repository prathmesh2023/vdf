from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from django.urls import re_path as url



urlpatterns = [
    path("", views.home, name="home"),
    path("department/aplied_science", views.aplied_science, name="aplied_science"),
    path("gallery", views.gallery, name="gallery"),
    path("pages/<str:link>", views.pages, name="pages"),
    path("trainningap", views.trainningap, name="trainningap"),
    path("library", views.library, name="library"),
    path("workshop", views.workshop, name="workshop"),
    path("placement2021", views.placement2021, name="placement2021"),
    path("placement2022", views.placement2022, name="placement2022"),

    
    path("registration",views.registration, name="registration"),
    path("news/<str:link>", views.news, name="news"),
    path("mou/<str:link>", views.mou, name="mou"),
    path("mous",views.mous, name="mous"),
    path("contact_us",views.contact_us, name="contact_us"),


# abot
    path("aboutvdf", views.aboutvdf, name="aboutvdf"),
    path("our_inspiration", views.our_inspiration, name="our_inspiration"),
    path("pmassage", views.pmassage, name="pmassage"),
    path("primassage", views.primassage, name="primassage"),

    path("feedback", views.feedback, name="feedback"),

    
    


# department

    path("about_as", views.about_as, name="about_as"),
    path("ce", views.ce, name="ce"),
    path("co", views.co, name="co"),
    path("el", views.el, name="el"),
    path("et", views.et, name="et"),
    path("me", views.me, name="me"),

# faculties

   
    path("facce", views.facce, name="facce"),
    path("facco", views.facco, name="facco"),
    path("facel", views.facel, name="facel"),
    path("facet", views.facet, name="facet"),
    path("facme", views.facme, name="facme"),
    path("facas", views.facas, name="facas"),

    path("ilad", views.ilad, name="ilad"),
    path("ilfy", views.ilfy, name="ilfy"),
    path("ildse", views.ildse, name="ildse"),

    

# naac

    path("aqar2019_2020", views.aqar2019_2020, name="aqar2019_2020"),
    path("aqar2020_2021", views.aqar2020_2021, name="aqar2020_2021"),
    path("naac", views.mnaac, name="nacc"),



    path("aluminireg", views.aluminireg, name="aluminireg"),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

