from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.db.models import Q
from django.utils.timezone import datetime
from .models import *
from .forms import *
from main.views import *

# Create your views here.

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('../')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('email')
				messages.success(request, 'Account was created for ' + user)

				return redirect('../')


		context = {'form':form}
		return render(request, 'accounts/register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		if request.user.admin==True:
			return redirect('../monitor')
		elif request.user.staff==True:
			return redirect('../faculty')
		return redirect('../student')
	else:
		if request.method == 'POST':
			username = request.POST.get('email')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				if user.admin==True:
					return redirect('../monitor')
				if user.staff==True:
					return redirect('../faculty')
				return redirect('../student')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('../')
