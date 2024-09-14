from django.urls import path
from . import views
urlpatterns = [
    path('home/<str: name/>', views.home , name = "home"),
    path("<int:id>/",views.post, name ='post')
]