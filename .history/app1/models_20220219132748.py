from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField
from django.db.models.aggregates import Max
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
    course=models.CharField(max_length=150, default="")
    is_pcm= models.CharField(max_length=150, default="")
    cast= models.CharField(max_length=150, default="")
    mission_branch= models.CharField(max_length=150, default="")
    is_loan= models.CharField(max_length=150, default="")
    is_instalment= models.CharField(max_length=150, default="")


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

    logo = models.ImageField( upload_to="images/mou/logo")

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