from django.db import models

# Create your models here.
class HBsAg(models.Model):
	SampleNo1_OD=models.TextField(blank=True)
	SampleNo2_OD=models.TextField(blank=True)
	SampleNo3_OD=models.TextField(blank=True)
	SampleNo4_OD=models.TextField(blank=True)
	SampleNo5_OD=models.TextField(blank=True)
	SampleNo1_Result=models.TextField(blank=True)
	SampleNo2_Result=models.TextField(blank=True)
	SampleNo3_Result=models.TextField(blank=True)
	SampleNo4_Result=models.TextField(blank=True)
	SampleNo5_Result=models.TextField(blank=True)
	Methodology=models.TextField(blank=True)
	CutOffValue=models.TextField(blank=True)

class Anti_HIV(models.Model):
	SampleNo1_OD=models.TextField(blank=True)
	SampleNo2_OD=models.TextField(blank=True)
	SampleNo3_OD=models.TextField(blank=True)
	SampleNo4_OD=models.TextField(blank=True)
	SampleNo5_OD=models.TextField(blank=True)
	SampleNo1_Result=models.TextField(blank=True)
	SampleNo2_Result=models.TextField(blank=True)
	SampleNo3_Result=models.TextField(blank=True)
	SampleNo4_Result=models.TextField(blank=True)
	SampleNo5_Result=models.TextField(blank=True)
	Methodology=models.TextField(blank=True)
	CutOffValue=models.TextField(blank=True)

class Anti_HCV(models.Model):
	SampleNo1_OD=models.TextField(blank=True)
	SampleNo2_OD=models.TextField(blank=True)
	SampleNo3_OD=models.TextField(blank=True)
	SampleNo4_OD=models.TextField(blank=True)
	SampleNo5_OD=models.TextField(blank=True)
	SampleNo1_Result=models.TextField(blank=True)
	SampleNo2_Result=models.TextField(blank=True)
	SampleNo3_Result=models.TextField(blank=True)
	SampleNo4_Result=models.TextField(blank=True)
	SampleNo5_Result=models.TextField(blank=True)
	Methodology=models.TextField(blank=True)
	CutOffValue=models.TextField(blank=True)

class Syphilis(models.Model):
	SampleNo1_OD=models.TextField(blank=True)
	SampleNo2_OD=models.TextField(blank=True)
	SampleNo3_OD=models.TextField(blank=True)
	SampleNo4_OD=models.TextField(blank=True)
	SampleNo5_OD=models.TextField(blank=True)
	SampleNo1_Result=models.TextField(blank=True)
	SampleNo2_Result=models.TextField(blank=True)
	SampleNo3_Result=models.TextField(blank=True)
	SampleNo4_Result=models.TextField(blank=True)
	SampleNo5_Result=models.TextField(blank=True)
	Methodology=models.TextField(blank=True)
	CutOffValue=models.TextField(blank=True)

class Malaria_Parasite(models.Model):
	SampleNo6=models.TextField(blank=True)
	SampleNo7=models.TextField(blank=True)
	Methodology=models.TextField(blank=True)

class Haemoglobin(models.Model):
	SampleNo6=models.TextField(blank=True)
	SampleNo7=models.TextField(blank=True)
	Methodology=models.TextField(blank=True)

class Direct_Anti_globin_Test(models.Model):
	SampleNo6=models.BooleanField(default=True)

class ABO_and_Rh_on_Patient_S6(models.Model):
	cell_forward_typing_method_used=models.TextField(blank=True)
	Anti_A=models.IntegerField(default=0)
	Anti_B=models.IntegerField(default=0)
	Anti_ABpositive=models.IntegerField(default=0)
	Anti_D=models.IntegerField(default=0)
	serum_reverse_group_method_used=models.TextField(blank=True)
	Acells=models.IntegerField(default=0)
	Bcells=models.IntegerField(default=0)
	Ocells=models.IntegerField(default=0)
	Result=models.TextField(blank=True)
			
class ABO_and_Rh_on_Donors(models.Model):
	cell_forward_typing_method_used=models.TextField(blank=True)
	serum_reverse_group_method_used=models.TextField(blank=True)
	Anti_A_S7=models.IntegerField(default=0)
	Anti_B_S7=models.IntegerField(default=0)
	Anti_ABpositive_S7=models.IntegerField(default=0)
	Anti_D_S7=models.IntegerField(default=0)	
	Acells_S7=models.IntegerField(default=0)
	Bcells_S7=models.IntegerField(default=0)
	Ocells_S7=models.IntegerField(default=0)
	Result_S7=models.TextField(blank=True)
	#
	Anti_A_S8=models.IntegerField(default=0)
	Anti_B_S8=models.IntegerField(default=0)
	Anti_ABpositive_S8=models.IntegerField(default=0)
	Anti_D_S8=models.IntegerField(default=0)	
	Acells_S8=models.IntegerField(default=0)
	Bcells_S8=models.IntegerField(default=0)
	Ocells_S8=models.IntegerField(default=0)
	Result_S8=models.TextField(blank=True)
	#
	Anti_A_S9=models.IntegerField(default=0)
	Anti_B_S9=models.IntegerField(default=0)
	Anti_ABpositive_S9=models.IntegerField(default=0)
	Anti_D_S9=models.IntegerField(default=0)	
	Acells_S9=models.IntegerField(default=0)
	Bcells_S9=models.IntegerField(default=0)
	Ocells_S9=models.IntegerField(default=0)
	Result_S9=models.TextField(blank=True)

class Compatibility_Testing(models.Model):
	MethodUsed=models.TextField(blank=True)
	SampleNo7D_and_10R_Saline_Room_temp=models.TextField(blank=True)
	SampleNo7D_and_10R_Additive_Room_temp=models.TextField(blank=True)
	SampleNo7D_and_10R_Additive_37degC=models.TextField(blank=True)
	SampleNo7D_and_10R_IAHG=models.TextField(blank=True)
	Would_transfer7to10=models.BooleanField(default=True)

	SampleNo8D_and_11R_Saline_Room_temp=models.TextField(blank=True)
	SampleNo8D_and_11R_Additive_Room_temp=models.TextField(blank=True)
	SampleNo8D_and_11R_Additive_37degC=models.TextField(blank=True)
	SampleNo8D_and_11R_IAHG=models.TextField(blank=True)
	Would_transfer8to11=models.BooleanField(default=True)

	SampleNo9D_and_12R_Saline_Room_temp=models.TextField(blank=True)
	SampleNo9D_and_12R_Additive_Room_temp=models.TextField(blank=True)
	SampleNo9D_and_12R_Additive_37degC=models.TextField(blank=True)
	SampleNo9D_and_12R_IAHG=models.TextField(blank=True)
	Would_transfer9to12=models.BooleanField(default=True)
	
	Specifiy_additive=models.TextField(blank=True)
	Specifiy_other_method=models.TextField(blank=True)					