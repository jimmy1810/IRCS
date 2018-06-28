from django import forms
from .models import Beqas

class BeqasCreate(forms.ModelForm):
	class Meta:
		model=Beqas
		fields=['patientId','Methodology_HBsAg','CutOffValue_HBsAg','SampleNo1_OD_HBsAg','SampleNo2_OD_HBsAg','SampleNo3_OD_HBsAg','SampleNo4_OD_HBsAg','SampleNo5_OD_HBsAg','SampleNo1_Result_HBsAg','SampleNo2_Result_HBsAg','SampleNo3_Result_HBsAg','SampleNo4_Result_HBsAg','SampleNo5_Result_HBsAg','Methodology_Anti_HIV','CutOffValue_Anti_HIV','SampleNo1_OD_Anti_HIV','SampleNo2_OD_Anti_HIV','SampleNo3_OD_Anti_HIV','SampleNo4_OD_Anti_HIV','SampleNo5_OD_Anti_HIV','SampleNo1_Result_Anti_HIV','SampleNo2_Result_Anti_HIV','SampleNo3_Result_Anti_HIV','SampleNo4_Result_Anti_HIV','SampleNo5_Result_Anti_HIV','Methodology_Anti_HCV','CutOffValue_Anti_HCV','SampleNo1_OD_Anti_HCV','SampleNo2_OD_Anti_HCV','SampleNo3_OD_Anti_HCV','SampleNo4_OD_Anti_HCV','SampleNo5_OD_Anti_HCV','SampleNo1_Result_Anti_HCV','SampleNo2_Result_Anti_HCV','SampleNo3_Result_Anti_HCV','SampleNo4_Result_Anti_HCV','SampleNo5_Result_Anti_HCV','Methodology_Syphilis','CutOffValue_Syphilis','SampleNo1_OD_Syphilis','SampleNo2_OD_Syphilis','SampleNo3_OD_Syphilis','SampleNo4_OD_Syphilis','SampleNo5_OD_Syphilis','SampleNo1_Result_Syphilis','SampleNo2_Result_Syphilis','SampleNo3_Result_Syphilis','SampleNo4_Result_Syphilis','SampleNo5_Result_Syphilis','Methodology_Malaria_Parasite','SampleNo6_Malaria_Parasite','SampleNo7_Malaria_Parasite','Methodology_Haemoglobin','SampleNo6_Haemoglobin','SampleNo7_Haemoglobin','SampleNo6_Direct_Anti_globin_Test','cft_method_ABO_and_Rh_on_Patient_S6','Anti_A_S6','Anti_B_S6','Anti_ABpositive_S6','Anti_D_S6','Acells_S6','Bcells_S6','Ocells_S6','Result_S6','method_ABO_and_Rh_on_Donors','Anti_A_S7','Anti_B_S7','Anti_ABpositive_S7','Anti_D_S7','Acells_S7','Bcells_S7','Ocells_S7','Result_S7','Anti_A_S8','Anti_B_S8','Anti_ABpositive_S8','Anti_D_S8','Acells_S8','Bcells_S8','Ocells_S8','Result_S8','Anti_A_S9','Anti_B_S9','Anti_ABpositive_S9','Anti_D_S9','Acells_S9','Bcells_S9','Ocells_S9','Result_S9','MethodUsed','SampleNo7D_and_10R_Saline_Room_temp','SampleNo7D_and_10R_Additive_Room_temp','SampleNo7D_and_10R_Additive_37degC','SampleNo7D_and_10R_IAHG','Would_transfer7to10','SampleNo8D_and_11R_Saline_Room_temp','SampleNo8D_and_11R_Additive_Room_temp','SampleNo8D_and_11R_Additive_37degC','SampleNo8D_and_11R_IAHG','Would_transfer8to11','SampleNo9D_and_12R_Saline_Room_temp','SampleNo9D_and_12R_Additive_Room_temp','SampleNo9D_and_12R_Additive_37degC','SampleNo9D_and_12R_IAHG','Would_transfer9to12','Specifiy_additive','Specifiy_other_method',]

class Beqassearch(forms.Form):
	patId=forms.IntegerField()