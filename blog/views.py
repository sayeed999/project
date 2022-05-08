from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
	 

	return render (request,'html/homepage.html')



def profile(request,name):
	context={
		'name'=name
	}
	return render (request,'html/profile.html',context)