from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from helpers import *
from django.contrib.auth.models import User
from django.http import HttpResponse
import datetime

def home(request):    
    
    return render_to_response("home.html",{'datetime':datetime.datetime.now()},
            context_instance=RequestContext(request))

def about(request):
    return render_to_response("about.html",{'datetime':datetime.datetime.now()},
            context_instance=RequestContext(request))

def contact(request):    
    contact = {
		'name': 'Stanley Semilla',
		'phone_number': '639272765841',
		'email':'semillastan@gmail.com',
		'url':'http://semillastan.com',
		'company':'N/A'
    }
    return render_to_response("contact.html",{'contact':contact},
            context_instance=RequestContext(request))
