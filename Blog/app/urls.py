from django.urls import path
from . import views

urlpatterns =[
    path('', views.homepage_view, name='homepage'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('post/new/', views.create_post, name='create_post'),
]