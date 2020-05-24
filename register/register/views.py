from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
	return render(request, 'base.html')

def register(request):
	form = None
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		email = request.POST.get('email')
		if User.objects.filter(email=email).exists():
			messages.error(request, 'Пользователь с єтим адресом уже зарегестрирован!')
		else:
			if form.is_valid():

				ins = form.save()
				username = form.cleaned_data['username']
				password = form.cleaned_data['password1']

				user = authenticate(username=username, password=password, email=email)
				ins.email = email
				ins.save()
				form.save_m2m()
				messages.success(request, 'Вы успешно заресестрировались')
				return redirect('/')
			

	else:
		form = UserRegisterForm()

	context = {'form': form}
	return render(request, 'register.html', context)