from django.db import models

# Create your models here.

class Contact(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField()
     message = models.TextField()
     subject= models.CharField(max_length=100)

     def __str__(self):
         return self.name