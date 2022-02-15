from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
	return render(request, 'user_example/index.html')

def register(request):
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save() #creates a new user and saves it on the DB because the form is based off the User Model
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password = password)
			login(request, user)
			return redirect('index')
	form = UserCreationForm()
	context = {'form' : form}
	return render(request, 'registration/register.html', context)
