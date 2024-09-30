from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Posts , Comment
from .forms import PostForm , CommentForm 
from django.shortcuts import render

def homepage_view(request):
    return render(request, 'app/homepage.html')  # Render a template for homepage


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

    #render(request, template_name, context=None, content_type=None, status=None, using=None)

    return render(request, "post_list.html" ,{'posts':posts}) #context dictionary where keys represent the variable names that will be accessible inside the template



# View for creating a new blog post
@login_required
def create_post(request):
    if request.method == "POST":
        form  = PostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            
            return redirect('post_list')
        
    else :
        form = PostForm()
    
    return render(request , "create_blog.html", {'form': form})



# View for blog post details (and adding comments)
    
def blog_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk) #fetches a single blog post from the database using its primary key (pk)
    comments = post.comments.all() #retrieves all comments associated with the retrieved blog post (post)
    #assumes there's a ForeignKey relationship between the Comment model and the Posts model
    #related_name='comments' allows you to access the comments

    if request.method == "POST":
        form =CommentForm(request.POST) #A CommentForm is created using the data submitted by the user (request.POST).
        if form.is_valid():
            comment = form.save(commit=False)
            #commit=False allows you to modify the comment before saving it to the database,
            #which is useful when you need to add extra fields (like the post and author).

            comment.post = post
            comment.author= request.user
            comment.save()
            return redirect("blog_detail" , pk =post.pk)
        
    else:
        form = CommentForm()
    return render(request ,'blog_detail.html', {'post': post, 'comments': comments, 'form': form} )

