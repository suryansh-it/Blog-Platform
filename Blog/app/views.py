from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

posts =[]
def home(request):
    html = ""
    for post in posts :
        html += f'''
                    <div>
                    <a href= "/post/{post['id']}/">
                    <h1>{post['id']} - {post['title']}</h1></a>
                    <p>{post['content']}</p>
                    </div>'''

    return HttpResponse(html)

def post(request,id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True  
            break  
    if valid_id:
        html = f'''<h1>{post_dict['title']}</h1>
                <p>{post_dict['content']}</p>'''
        return HttpResponse(html)
    else :
        return HttpResponseNotFound("Post not Avilable")
    

def something(request, id):
    url = reverse("post" , args=[id])
    return HttpResponseRedirect(url)
# Create your views here.
