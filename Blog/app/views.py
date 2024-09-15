from django.shortcuts import render
from django.http import  Http404
# from django.urls import reverse

posts =[]
categories = [
    "Programming",
    "Food",
    "Travel"
]
def home(request):  #parameter = request
    html = ""
    for post in posts :
        html += f'''
                    <div>
                    <a href= "/post/{post['id']}/">
                    <h1>{post['id']} - {post['title']}</h1></a>
                    <p>{post['content']}</p>
                    </div>'''

    return render(request , "app/home.html", {'posts': posts , 'categories' : categories})  #should be same as parameter

def post(request,id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True  
            break  
    if valid_id:
        
        return render(request , "app/post.html", {'post_dict' : post, 'categories' : categories})
    else :
        raise Http404()
    

# def something(request, id):
#     url = reverse("post" , args=[id]) #url name and id as argument
#     return HttpResponseRedirect(url)
# Create your views here.
