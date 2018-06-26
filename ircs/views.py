from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from .forms import BeqasCreate


def index(request):
	return HttpResponse('<h1>Welcome</h1>')


def showform(request):
	if request.method=="POST":
		form=BeqasCreate(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/ircs/index') #tera koi path dal dena

	else :
		form=BeqasCreate()
		return HttpResponseRedirect('/ircs/index') 

	return render(request,'ircs/beqas_form.html',{'form':form})
	
