from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q




# Create your views here.

def sign_up(request):
	if request.method == "POST":
		print("form submitted")
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = User.objects.create_user(username=username, password=password)
		user.save()

	return render(request, 'theplug/sign_up.html', {})


def login_view(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		try:
			user = User.objects.get(Q(username=username) | Q(email=username))
			if user.check_password(password):
				print("Login successful")
				login(request, user)
			else:
				print("Password incorrect")
		except User.DoesNotExist:
			print("User does not exist!")
		if user:
			return render(request, 'theplug/dashboard.html', {'username':request.user})
	return render(request, 'theplug/login.html', {})


def dashboard(request):
	if request.user.is_authenticated:
		return render(request, 'theplug/dashboard.html', {'username':request.user})
	else:
		return render(request, 'theplug/login.html', {})

def logout_view(request):
	logout(request)
	return render(request, "theplug/login.html", {})

