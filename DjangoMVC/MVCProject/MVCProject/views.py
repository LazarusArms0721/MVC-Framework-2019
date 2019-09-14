from django.http import HttpResponse
from django.shortcuts import render

def aboutView(request):
	# return HttpResponse('about')
	return render(request, 'about.html')


def homeView(request):
	# return HttpResponse('home')
	return render (request, 'home.html')