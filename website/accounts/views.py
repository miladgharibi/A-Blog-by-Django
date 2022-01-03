from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.
class LoginView(View):
	def get(self, request):
		context = {
			'form': AuthenticationForm()
		}
		return render(request, 'registration/login.html', context)

	def post(self, request):
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, 'You are successfuly logged in :)')
				return redirect('core:home')
			else:
				messages.error(request, 'Your username or password is incorrect')
				return redirect('login')
		
		messages.error(request, 'Your username or password is incorrect')
		return redirect('login')


class SignUpView(View):
	def get(self, request):
		context = {
			'form': UserCreationForm()
		}
		return render(request, 'registration/signup.html', context)


	def post(self, request):
		form = UserCreationForm(request.POST or None)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, 'Your account was successfuly created :)')
			return redirect('core:home')
		else:
			messages.error(request, 'Please try again!')
			return redirect('signup')

