from django.contrib import admin

# Register your models here.
from .models import Region, Donor, Receiver
#Rgister your models here.
admin.site.register(Region)
admin.site.register(Donor)
admin.site.register(Receiver)
