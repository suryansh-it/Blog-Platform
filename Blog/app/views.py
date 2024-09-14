from django.shortcuts import render

posts =[]
def home(request):
    html = ""
    for post in posts :
        html += f'''
                    <div><h1>{post['id']} - {post['title']}</h1>
                    <p>{post['content']}</p>
                    </div>'''

    return HttpResponse(html)

def post(request,id):
    return HttpResponse(id)
# Create your views here.
