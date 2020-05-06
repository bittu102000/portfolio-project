from django.shortcuts import render

from .models import Jobs

def home(request):
	jobss = Jobs.objects
	return render(request,'jobs/home.html', {'jobss':jobss})