from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from .forms import BeqasCreate,Beqassearch,Beqascycle
from .models import Beqas


def index(request):
	return HttpResponse('<h1>Welcome</h1>')

def searchid(request):
	if request.method=="POST":
		form=Beqassearch(request.POST)
		if form.is_valid():
			val = int(form['patId'].value())
			try:
				b = Beqas.objects.get(patientId = val)
				return render(request,'ircs/beqasdisplay.html',{'des':b})
			except:
				return HttpResponse('<h1> ID not found</h1>')
		else:
			form=Beqassearch()
	else:
		form = Beqassearch()
		return render(request,'ircs/searchid.html',{'form':form})

def beqas_form(request):
	if request.method=="POST":
		form=BeqasCreate(request.POST)
		if form.is_valid():
			form.save()
			form=BeqasCreate()
			return render(request,'ircs/beqas.html',{'form':form})
		else:
			form=BeqasCreate()
			return render(request,'ircs/beqas.html',{'form':form})

	else :
		form=BeqasCreate()

	return render(request,'ircs/beqas.html',{'form':form})
	
def searchby(request):
	if request.method=="POST":
		form=Beqascycle(request.POST)
		if form.is_valid():
			val = int(form['cyno'].value())
			yr= int(form['year'].value())
			try:
				b = Beqas.objects.filter(cycleno = val , year= yr)
				return render(request,'ircs/cycledisplay.html',{'des':b})
			except:
				return HttpResponse('<h1>Cycle Number not found</h1>')
		else:
			form=Beqascycle()
	else:
		form = Beqascycle()
		return render(request,'ircs/searchby.html',{'form':form})


