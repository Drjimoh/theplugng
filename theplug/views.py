from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from theplug.models import Post




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

def add_post(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			title = request.POST.get("title", None)
			body = request.POST.get("body", None)
			image = request.POST.get("file", None)
			new_post = Post.objects.create(title=title, body=body, image=image)
			new_post.save()
			posts = Post.objects.all()[:10]
			return render(request, 'theplug/created_success.html', {'posts':posts})
		else:
			return render(request, 'theplug/create_post.html', {})
	else:
		return render(request, 'theplug/login.html', {})

def view_post(request):
	posts = Post.objects.all()[:10]
	return render(request, "theplug/posts.html", {'posts':posts})

def delete_post(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			# handle form submission
			pass
		else:
			return render(request, 'theplug/posts.html', {})
	else:
		return render(request, 'theplug/login.html', {})

def edit_post(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			# handle form submission
			pass
		else:
			return render(request, 'theplug/edit_post.html', {})
	else:
		return render(request, 'theplug/login.html', {})


def created_success(request):
	posts = Post.objects.all()[:10]
	return render(request, "theplug/created_success.html", {'posts':posts})

def logout_view(request):
	logout(request)
	return render(request, "theplug/login.html", {})

