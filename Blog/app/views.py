from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

posts =[]
def home(request):  #parameter = request
    html = ""
    for post in posts :
        html += f'''
                    <div>
                    <a href= "/post/{post['id']}/">
                    <h1>{post['id']} - {post['title']}</h1></a>
                    <p>{post['content']}</p>
                    </div>'''

    return render(request , "app/home.html", {'posts': posts , 'username' : 'suryansh'})  #should be same as parameter

def post(request,id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True  
            break  
    if valid_id:
        
        return render(request , "app/post.html", {'post_dict' : post})
    else :
        return HttpResponseNotFound("Post not Avilable")
    

def something(request, id):
    url = reverse("post" , args=[id]) #url name and id as argument
    return HttpResponseRedirect(url)
# Create your views here.
