from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Posts , Comment
from .forms import PostForm , CommentForm 



# user registration view

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else :
        form = UserCreationForm()
    return render(request , "signup.html",{"form": form})



# View for listing all blog posts

def post_list(request):
    posts = Posts.objects.all().order_by("-dated")
    return render(request, "post_list.html" ,{'posts':posts})