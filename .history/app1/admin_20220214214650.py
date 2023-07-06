from django.contrib import admin
from .models import gallery
from .models import page,mediaimg
from .models import mediafile
from .models import registration
from .models import news,mou,viewer
# Register your models here.


admin.site.register(page)

admin.site.register(gallery)

admin.site.register(mediaimg)

admin.site.register(mediafile)

admin.site.register(registration)

admin.site.register(news)

admin.site.register(mou)

admin.site.register(viewer)