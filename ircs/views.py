from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from .forms import BeqasCreate,Beqassearch
from .models import Beqas


def index(request):
	return HttpResponse('<h1>Welcome</h1>')

def searchid(request):
	form_class=Beqassearch
	form = form_class(request.POST or None)
	if request.method=="POST":
		form=Beqassearch(request.POST)
		if form.is_valid():
			beqasall=Beqas.objects.all()
			flag=0
			for des in beqasall:
				if des.patientId==form.patId:
					flag=1
					return render(request,'ircs/beqasdisplay.html',{'des':des})
			if flag==0:
				return HttpResponse('<h1> elem not found</h1>')
		else:
			form=Beqassearch()
	
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
	
