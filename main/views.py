from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import NewUserForm
from .forms import PostForm, SearchForm
from .models import Post, search
from django.utils import timezone
from datetime import date, timedelta
from django.db.models import Q

# Create your views here.
def homepage(request):
	return render(request=request,
		          template_name="main/home.html")
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New account created: {username}")
			return redirect("main:register")
		else:
			for msg in form.error_messages:
				messages.error(request,f"{msg}:{form.error_messages[msg]}")
	form = NewUserForm
	return render(request,"main/register.html", context={"form":form})
def logout_request(request):
	logout(request)
	messages.info(request, "Logged out succesfully!")
	return redirect("main:login")
def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return HttpResponseRedirect(reverse("main:thisweek"))
				
				
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")

	form = AuthenticationForm()
	return render(request,
		          "main/login.html",
				  context={"form":form})
def pub_entry(request):
	posts = Post.objects.filter(public_or_private="public").order_by('published_date')
	return render(request=request, template_name="main/pub_entry.html", context={'posts': posts})
def add_entry(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("main:thisweek")
    else:
        form = PostForm()
    return render(request=request, template_name="main/add_entry.html", context={'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('main:allentry')
    else:
        form = PostForm(instance=post)
    return render(request=request, template_name="main/add_entry.html", context={'form': form})
def thisweek(request):
	user = request.user
	d=date.today()-timedelta(days=7)
	posts = Post.objects.filter(author = request.user, published_date__gte=d, published_date__lte=timezone.now()).order_by('published_date')
	return render(request=request, template_name="main/thisweek.html", context={'posts': posts, 'user':user})
def allentry(request):
	user = request.user
	posts = Post.objects.filter(author = request.user).order_by('published_date')
	return render(request=request, template_name="main/allentry.html", context={'posts': posts, 'user':user})
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('main:allentry')
def Search(request):
	if request.method == "GET":
		form = SearchForm(request.GET)
		if form.is_valid():
			auth=form.cleaned_data['author']
			tit=form.cleaned_data['title']
			posts = Post.objects.filter(writer=auth, title=tit, public_or_private="public")
			return render(request=request, template_name="main/results.html", context={'posts': posts})
	else:
		form = SearchForm()
	return render(request=request, template_name="main/Search.html", context={'form': form})


