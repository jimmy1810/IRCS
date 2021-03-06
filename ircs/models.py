from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from datetime import date

# Create your models here.
class Beqas(models.Model):
	choice=(('n','neg'),('1','1'),('2','2'),('3','3'),('4','4'))

	#im=models.ImageField()
	cycleno=models.IntegerField(default=1)
	year=models.IntegerField(default=2018)
	#date=models.DateField(("Date"), default=date.today)
	patientId=models.PositiveIntegerField(default=0,unique=True,validators=[MinValueValidator(1)])
	Methodology_HBsAg=models.CharField(blank=True , max_length=100)
	CutOffValue_HBsAg=models.CharField(blank=True , max_length=100)
	SampleNo1_OD_HBsAg=models.CharField(blank=True , max_length=100)
	SampleNo2_OD_HBsAg=models.CharField(blank=True , max_length=100)
	SampleNo3_OD_HBsAg=models.CharField(blank=True , max_length=100)
	SampleNo4_OD_HBsAg=models.CharField(blank=True , max_length=100)
	SampleNo5_OD_HBsAg=models.CharField(blank=True , max_length=100)
	SampleNo1_Result_HBsAg=models.CharField(blank=True , max_length=100)
	SampleNo2_Result_HBsAg=models.CharField(blank=True , max_length=100)
	SampleNo3_Result_HBsAg=models.CharField(blank=True , max_length=100)
	SampleNo4_Result_HBsAg=models.CharField(blank=True , max_length=100)
	SampleNo5_Result_HBsAg=models.CharField(blank=True , max_length=100)
	

	Methodology_Anti_HIV=models.CharField(blank=True , max_length=100)
	CutOffValue_Anti_HIV=models.CharField(blank=True , max_length=100)
	SampleNo1_OD_Anti_HIV=models.CharField(blank=True , max_length=100)
	SampleNo2_OD_Anti_HIV=models.CharField(blank=True , max_length=100)
	SampleNo3_OD_Anti_HIV=models.CharField(blank=True , max_length=100)
	SampleNo4_OD_Anti_HIV=models.CharField(blank=True , max_length=100)
	SampleNo5_OD_Anti_HIV=models.CharField(blank=True , max_length=100)
	SampleNo1_Result_Anti_HIV=models.CharField(blank=True , max_length=100)
	SampleNo2_Result_Anti_HIV=models.CharField(blank=True , max_length=100)
	SampleNo3_Result_Anti_HIV=models.CharField(blank=True , max_length=100)
	SampleNo4_Result_Anti_HIV=models.CharField(blank=True , max_length=100)
	SampleNo5_Result_Anti_HIV=models.CharField(blank=True , max_length=100)
	

	Methodology_Anti_HCV=models.CharField(blank=True , max_length=100)
	CutOffValue_Anti_HCV=models.CharField(blank=True , max_length=100)
	SampleNo1_OD_Anti_HCV=models.CharField(blank=True , max_length=100)
	SampleNo2_OD_Anti_HCV=models.CharField(blank=True , max_length=100)
	SampleNo3_OD_Anti_HCV=models.CharField(blank=True , max_length=100)
	SampleNo4_OD_Anti_HCV=models.CharField(blank=True , max_length=100)
	SampleNo5_OD_Anti_HCV=models.CharField(blank=True , max_length=100)
	SampleNo1_Result_Anti_HCV=models.CharField(blank=True , max_length=100)
	SampleNo2_Result_Anti_HCV=models.CharField(blank=True , max_length=100)
	SampleNo3_Result_Anti_HCV=models.CharField(blank=True , max_length=100)
	SampleNo4_Result_Anti_HCV=models.CharField(blank=True , max_length=100)
	SampleNo5_Result_Anti_HCV=models.CharField(blank=True , max_length=100)
	

	Methodology_Syphilis=models.CharField(blank=True , max_length=100)
	CutOffValue_Syphilis=models.CharField(blank=True , max_length=100)
	SampleNo1_OD_Syphilis=models.CharField(blank=True , max_length=100)
	SampleNo2_OD_Syphilis=models.CharField(blank=True , max_length=100)
	SampleNo3_OD_Syphilis=models.CharField(blank=True , max_length=100)
	SampleNo4_OD_Syphilis=models.CharField(blank=True , max_length=100)
	SampleNo5_OD_Syphilis=models.CharField(blank=True , max_length=100)
	SampleNo1_Result_Syphilis=models.CharField(blank=True , max_length=100)
	SampleNo2_Result_Syphilis=models.CharField(blank=True , max_length=100)
	SampleNo3_Result_Syphilis=models.CharField(blank=True , max_length=100)
	SampleNo4_Result_Syphilis=models.CharField(blank=True , max_length=100)
	SampleNo5_Result_Syphilis=models.CharField(blank=True , max_length=100)
	

	Methodology_Malaria_Parasite=models.CharField(blank=True , max_length=100)
	SampleNo6_Malaria_Parasite=models.CharField(blank=True , max_length=100)
	SampleNo7_Malaria_Parasite=models.CharField(blank=True , max_length=100)


	Methodology_Haemoglobin=models.CharField(blank=True , max_length=100)
	SampleNo6_Haemoglobin=models.CharField(blank=True , max_length=100)
	SampleNo7_Haemoglobin=models.CharField(blank=True , max_length=100)

	SampleNo6_Direct_Anti_globin_Test=models.BooleanField(default=True)

	cft_method_ABO_and_Rh_on_Patient_S6=models.CharField(blank=True , max_length=100)
	Anti_A_S6=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_B_S6=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_ABpositive_S6=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_D_S6=models.CharField(default="1" , max_length=40 ,choices=choice)
	Acells_S6=models.CharField(default="1" , max_length=40 ,choices=choice)
	Bcells_S6=models.CharField(default="1" , max_length=40 ,choices=choice)
	Ocells_S6=models.CharField(default="1" , max_length=40 ,choices=choice)
	Result_S6=models.CharField(blank=True , max_length=100)
			
	method_ABO_and_Rh_on_Donors=models.CharField(blank=True , max_length=100)
	Anti_A_S7=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_B_S7=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_ABpositive_S7=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_D_S7=models.CharField(default="1" , max_length=40 ,choices=choice)	
	Acells_S7=models.CharField(default="1" , max_length=40 ,choices=choice)
	Bcells_S7=models.CharField(default="1" , max_length=40 ,choices=choice)
	Ocells_S7=models.CharField(default="1" , max_length=40 ,choices=choice)
	Result_S7=models.CharField(blank=True , max_length=100)
	#
	Anti_A_S8=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_B_S8=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_ABpositive_S8=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_D_S8=models.CharField(default="1" , max_length=40 ,choices=choice)	
	Acells_S8=models.CharField(default="1" , max_length=40 ,choices=choice)
	Bcells_S8=models.CharField(default="1" , max_length=40 ,choices=choice)
	Ocells_S8=models.CharField(default="1" , max_length=40 ,choices=choice)
	Result_S8=models.CharField(blank=True , max_length=100)
	#
	Anti_A_S9=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_B_S9=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_ABpositive_S9=models.CharField(default="1" , max_length=40 ,choices=choice)
	Anti_D_S9=models.CharField(default="1" , max_length=40 ,choices=choice)	
	Acells_S9=models.CharField(default="1" , max_length=40 ,choices=choice)
	Bcells_S9=models.CharField(default="1" , max_length=40 ,choices=choice)
	Ocells_S9=models.CharField(default="1" , max_length=40 ,choices=choice)
	Result_S9=models.CharField(blank=True , max_length=100)

	MethodUsed=models.CharField(blank=True , max_length=100)
	SampleNo7D_and_10R_Saline_Room_temp=models.CharField(default="1" , max_length=40 ,choices=choice)
	SampleNo7D_and_10R_Additive_Room_temp=models.CharField(default="1" , max_length=40 ,choices=choice)
	SampleNo7D_and_10R_Additive_37degC=models.CharField(default="1" , max_length=40 ,choices=choice)
	SampleNo7D_and_10R_IAHG=models.CharField(default="1" , max_length=40 ,choices=choice)
	Would_transfer7to10=models.BooleanField(default=True)

	SampleNo8D_and_11R_Saline_Room_temp=models.CharField(default="1" , max_length=40 ,choices=choice)
	SampleNo8D_and_11R_Additive_Room_temp=models.CharField(default="1" , max_length=40 ,choices=choice)
	SampleNo8D_and_11R_Additive_37degC=models.CharField(default="1" , max_length=40 ,choices=choice)
	SampleNo8D_and_11R_IAHG=models.CharField(default="1" , max_length=40 ,choices=choice)
	Would_transfer8to11=models.BooleanField(default=True)

	SampleNo9D_and_12R_Saline_Room_temp=models.CharField(default="1" , max_length=40 ,choices=choice)
	SampleNo9D_and_12R_Additive_Room_temp=models.CharField(default="1" , max_length=40 ,choices=choice)
	SampleNo9D_and_12R_Additive_37degC=models.CharField(default="1" , max_length=40 ,choices=choice)
	SampleNo9D_and_12R_IAHG=models.CharField(default="1" , max_length=40 ,choices=choice)
	Would_transfer9to12=models.BooleanField(default=True)
	
	Specifiy_additive=models.CharField(blank=True , max_length=100)
	Specifiy_other_method=models.CharField(blank=True , max_length=100)	

