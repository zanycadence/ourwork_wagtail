from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import *

#def mentor_match(request,zipcode):
#	mentor =  Member.objects.filter(track_progress=3).filter(location = zipcode)
#	return mentor

#def mentor_match(request,zipcode,track2):
#	mentor =  Member.objects.filter(track_progress=3).filter(location = zipcode).filter(track=track_progress)
#	return mentor


def mentor_match(request):
	#zipcode = request.GET.get('location')
	#mentor =  Member.objects.filter(track_progress=3).filter(location = zipcode)
	mentor =  Member.objects.all().values()
	return mentor


def member(request,userid):
	return HttpResponse(<h1>This is the default user profile</h1>)