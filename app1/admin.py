from django.contrib import admin
from .models import feedback, gallery,feedback
from .models import page,mediaimg
from .models import mediafile
from .models import registration,contact
from .models import news,mou,viewer,naac,recruter,pop,alumini

from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(pop)
admin.site.register(page)

admin.site.register(gallery)

admin.site.register(mediaimg)

admin.site.register(mediafile)

admin.site.register(alumini)



@admin.register(registration)
class registrationAdmin(ImportExportModelAdmin):
    pass


@admin.register(contact)
class contactAdmin(ImportExportModelAdmin):
    pass


@admin.register(feedback)
class registrationAdmin(ImportExportModelAdmin):
    pass

    #resource_class = registration

#admin.site.register(registration,registrationAdmin)

admin.site.register(news)

admin.site.register(mou)

admin.site.register(naac)

admin.site.register(viewer)

admin.site.register(recruter)


