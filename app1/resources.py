from import_export import resources
from .models import registration,contact,feedback

class registrationResource(resources.ModelResource):

    class Meta:
        model = registration

class contactResource(resources.ModelResource):

    class Meta:
        model = contact

class feedbackResource(resources.ModelResource):

    class Meta:
        model = feedback