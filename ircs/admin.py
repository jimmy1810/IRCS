from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import HBsAg,Anti_HIV,Anti_HCV,Syphilis,Malaria_Parasite,Haemoglobin,ABO_and_Rh_on_Patient_S6,ABO_and_Rh_on_Donors,Compatibility_Testing
admin.site.register(HBsAg)
admin.site.register(Anti_HIV)
admin.site.register(Anti_HCV)
admin.site.register(Syphilis)
admin.site.register(Malaria_Parasite)
admin.site.register(Haemoglobin)
admin.site.register(ABO_and_Rh_on_Patient_S6)
admin.site.register(ABO_and_Rh_on_Donors)
admin.site.register(Compatibility_Testing)