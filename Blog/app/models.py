from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length= 200) 
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Link to the User model
    dated= models.DateTimeField(auto_now_add=True)


    def __str__(self) :
        return self.title  #return title when the obj is printed
    

class Comment(models.Model):
    post = models.ForeignKey(Posts , related_name="comments" , on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dated = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"Comment by {self.author} on {self.post}"