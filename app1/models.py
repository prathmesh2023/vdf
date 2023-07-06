
from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField
from django.db.models.aggregates import Max
from django.forms import IntegerField
# Create your models here.


class gallery(models.Model):
    img = models.ImageField(upload_to="app1/gallery/imgs", default="")
    caption = models.CharField('caption',max_length=400, default="", blank=True, null=True)

    
    def __str__(self):
        return self.caption


class page(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)

    body = RichTextField(blank=True, null=True)

    tags = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title


class mediaimg(models.Model):
    img = models.ImageField(upload_to="app1/media/imgs", default="")
    caption = models.CharField('caption',max_length=400, default="", blank=True, null=True)

    
    def __str__(self):
        return self.caption


class mediafile(models.Model):
    file = models.FileField(upload_to="app1/mediafiles/imgs", default="")
    caption = models.CharField('caption',max_length=400, default="", blank=True, null=True)

    
    def __str__(self):
        return self.caption



class registration(models.Model):
    name = models.CharField(max_length=150, default="")
    contact= models.CharField(max_length=150, default="")
    wp= models.CharField(max_length=150, default="")
    address= models.CharField(max_length=250, default="")
    course=models.CharField(max_length=150, default="" , null=True, blank=True)
    is_pcm= models.CharField(max_length=150, default="", null=True, blank=True)
    cast= models.CharField(max_length=150, default="", null=True, blank=True)
    mission_branch= models.CharField(max_length=150, default="", null=True, blank=True)
    is_loan= models.CharField(max_length=150, default="", null=True, blank=True)
    is_instalment= models.CharField(max_length=150, default="", null=True, blank=True)


    other_interasted_branches=models.CharField(max_length=150, blank=True, null=True)

    
    def __str__(self):
        return self.name



class news(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)

    body = RichTextField(blank=True, null=True)

    tags = models.CharField(max_length=500, null=True, blank=True)

    date = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title


class mou(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)

    logo = models.ImageField(blank=True, null=True , default='app1/media/imgs/blank_P9xJb40.png',  upload_to="images/mou/logo")

    body = RichTextField(blank=True, null=True)

    tags = models.CharField(max_length=500, null=True, blank=True)



    def __str__(self):
        return self.title
    
    



class naac(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)

    body = RichTextField(blank=True, null=True)

    tags = models.CharField(max_length=500, null=True, blank=True)



    def __str__(self):
        return self.title


class viewer(models.Model):

    ip=models.CharField(unique=True , max_length=500, default="" )

    # ttl = models.IntegerField()

    
    def __str__(self):
        return self.ip
    
    
class recruter(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self.name



    
class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    msg = models.CharField(max_length=200)
   
    
    def __str__(self):
        return self.name



class feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    wfrom=models.CharField(max_length=200)
    cmt=models.TextField()
   
    
    def __str__(self):
        return self.name

class pop(models.Model):
    img = models.ImageField(upload_to="app1/pop/imgs", default="")
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title


class alumini(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    yop = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    maritalstaus = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    address = models.TextField()
    aftergraduation =  models.TextField()
    memorie = models.TextField()

    def __str__(self):
        return self.name



