from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import login, REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.template import RequestContext

# Create your views here.

def login(request, redirect_field_name=REDIRECT_FIELD_NAME):
	redirect_to = request.GET.get(redirect_field_name, '')
	response = HttpResponse()
	if request.method == 'POST':
		if not redirect_to or '//' in redirect_to or ' ' in redirect_to:
			redirect_to = '/home/'
		username = request.POST.get('username', '')
		request.session['username'] = username
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			response.status = 302
			response['Location'] = redirect_to
			return response
			print "response"
		else:
			return HttpResponseRedirect('/register/')

	return render_to_response('login.html', {'form': request}, context_instance=RequestContext(request))
	
def register(request):
	return render(request, 'register.html', {'register': 'Register Page'})

def home(request):
	return render(request, 'blog/home.html', {'home': 'It\'s a home content' })