from django import forms
from .models import Beqas

class BeqasCreate(forms.ModelForm):
	class Meta:
		model=Beqas
		fields = "__all__"
		
class Beqassearch(forms.Form):
	patId=forms.IntegerField()