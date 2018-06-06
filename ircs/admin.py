from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import HBsAg,Anti_HIV,Anti_HCV,Syphilis,Malaria_Parasite,Haemoglobin,Direct_Anti_globin_Test,ABO_and_Rh_on_Patient,Sample_Identification_Scoring_on_Patient,ABO_and_Rh_on_Donors,Sample_Identification_Scoring_on_Donors,Compatibility_Testing,Sample_Identification_Scoring
admin.site.register(HBsAg)
admin.site.register(Anti_HIV)
admin.site.register(Anti_HCV)
admin.site.register(Syphilis)
admin.site.register(Malaria_Parasite)
admin.site.register(Haemoglobin)
admin.site.register(Direct_Anti_globin_Test)
admin.site.register(ABO_and_Rh_on_Patient)
admin.site.register(Sample_Identification_Scoring_on_Patient)
admin.site.register(ABO_and_Rh_on_Donors)
admin.site.register(Sample_Identification_Scoring_on_Donors)
admin.site.register(Compatibility_Testing)
admin.site.register(Sample_Identification_Scoring)