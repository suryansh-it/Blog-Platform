from django.db import models

# Create your models here.

class POsts(models.Model):
    title = models.CharField(max_length= 200) 
    content = models.TextField()
    dated= models.DateTimeField(auto_now_add=True)


    def __str__(self) :
        return self.title  #return title when the obj is printed