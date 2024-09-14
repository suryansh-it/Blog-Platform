from django.shortcuts import render
from django.http import HttpResponse

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
    for post in posts:
        if post['id'] == id:
            post_dict = post  
            break  
    
    html = f'''<h1>{post_dict['title']}</h1>
               <p>{post_dict['content']}</p>'''
    return HttpResponse(html)
# Create your views here.
