from django.db import models

# Create your models here.
class HBsAg(models.Model):
	SampleNo1=models.BooleanField(default=True)
	SampleNo2=models.BooleanField(default=True)
	SampleNo3=models.BooleanField(default=True)
	SampleNo4=models.BooleanField(default=True)
	SampleNo5=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)

class Anti_HIV(models.Model):
	SampleNo1=models.BooleanField(default=True)
	SampleNo2=models.BooleanField(default=True)
	SampleNo3=models.BooleanField(default=True)
	SampleNo4=models.BooleanField(default=True)
	SampleNo5=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)

class Anti_HCV(models.Model):
	SampleNo1=models.BooleanField(default=True)
	SampleNo2=models.BooleanField(default=True)
	SampleNo3=models.BooleanField(default=True)
	SampleNo4=models.BooleanField(default=True)
	SampleNo5=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)		

class Syphilis(models.Model):
	SampleNo1=models.BooleanField(default=True)
	SampleNo2=models.BooleanField(default=True)
	SampleNo3=models.BooleanField(default=True)
	SampleNo4=models.BooleanField(default=True)
	SampleNo5=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)

class Malaria_Parasite(models.Model):
	SampleNo6=models.BooleanField(default=True)
	SampleNo7=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)

class Haemoglobin(models.Model):
	SampleNo6_Sat_or_Not_Sat=models.BooleanField(default=True)
	SampleNo6_Mean_Value=models.IntegerField(default=0)
	SampleNo6_Your_Result=models.IntegerField(default=0)
	SampleNo6_Your_SDI_Value=models.IntegerField(default=0)
	SampleNo7_Sat_or_Not_Sat=models.BooleanField(default=True)
	SampleNo7_Mean_Value=models.IntegerField(default=0)
	SampleNo7_Your_Result=models.IntegerField(default=0)
	SampleNo7_Your_SDI_Value=models.IntegerField(default=0)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)

class Direct_Anti_globin_Test(models.Model):
	SampleNo6=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)

class ABO_and_Rh_on_Patient(models.Model):
	SampleNo6=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)

class Sample_Identification_Scoring_on_Patient(models.Model):
	SampleNo6=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)
			
class ABO_and_Rh_on_Donors(models.Model):
	SampleNo7=models.BooleanField(default=True)
	SampleNo8=models.BooleanField(default=True)
	SampleNo9=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)

class Sample_Identification_Scoring_on_Donors(models.Model):
	SampleNo7=models.BooleanField(default=True)
	SampleNo8=models.BooleanField(default=True)
	SampleNo9=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)

class Compatibility_Testing(models.Model):
	SampleNo7_and_10=models.BooleanField(default=True)
	SampleNo8_and_11=models.BooleanField(default=True)
	SampleNo9_and_12=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)

class Sample_Identification_Scoring(models.Model):
	SampleNo7_and_10=models.BooleanField(default=True)
	SampleNo8_and_11=models.BooleanField(default=True)
	SampleNo9_and_12=models.BooleanField(default=True)
	AchievableScore=models.IntegerField(default=0)
	YourScore=models.IntegerField(default=0)					