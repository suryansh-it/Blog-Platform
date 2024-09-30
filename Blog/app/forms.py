from django import forms
from .models import Posts, Comment

#creating new project form 

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title' , 'content '] 

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment 
        fields = ['content']