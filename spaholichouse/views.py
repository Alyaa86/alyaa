from django.shortcuts import render , redirect 
from .models import Service
from .forms import ServiceForm
from .forms import UserRegisterForm, LoginForm
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout


# Create your views here.
def list(request):
	service = Service.objects.all()
	service.order_by('name')
	context = {
		'services' : service
	}
	return render (request,'service_list.html' , context)

def detail(request, service_id):
	context = {
		'service' : Service.objects.get(id=service_id)
	}
	return render (request,'service_detail.html' , context)

def create(request):
	form = ServiceForm()
	if request.method == "POST":
		form = ServiceForm(request.POST)		
		if form.is_valid():
			form.save()
			return redirect('service_list')

	context = {
		'create_form' : form,
	}

	return render(request , 'create_form.html', context)


def update(request, service_id):
	service_object = Service.objects.get(id=service_id)
	form = ServiceForm(instance= service_object)
	if request.method == "POST":
		form = ServiceForm(request.POST, instance=service_object)
		if form.is_valid():
			form.save()
			return redirect('service_list')

	context = {
		'update_form' : form,
		'service' : service_object
	}

	return render(request , 'update_form.html', context)

def delete(request, service_id):
	Service.objects.get(id=service_id).delete()
	return redirect('service_list')


def signin(request):
	form=LoginForm()
	if request.method == "POST":
		form=LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect ("service_list")

	context = {
		'signin' : form,
	}
	return render (request, 'signin.html', context)

def signup(request):
	form=UserRegisterForm()
	if request.method == "POST":
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			login(request, user)
			return redirect ("service_list")

	context = {
		'signup' : form,
	}
	return render (request, 'signup.html', context)

def log_out(request):
	logout(request)
	return redirect("signin")
