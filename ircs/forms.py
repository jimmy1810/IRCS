from django import forms
from .models import Beqas

class BeqasCreate(forms.ModelForm):
	class Meta:
		model=Beqas
		fields = "__all__"
		
class Beqassearch(forms.Form):
	patId=forms.IntegerField()

class Beqascycle(forms.Form):
	cyno=forms.IntegerField(initial=1)	
	year=forms.IntegerField(initial=2018)