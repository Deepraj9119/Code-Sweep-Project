from django.db import models
from django.contrib.auth.models import User  # Optional, if you want to associate history with a user

# Create your models here.

class Contact(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField()
     message = models.TextField()
     subject= models.CharField(max_length=100)

     def __str__(self):
         return self.name

class History(models.Model):
    url = models.URLField()
    unused_resources = models.TextField()  # Store unused resources as a JSON string or plain text
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional

    def __str__(self):
        return f"History for {self.url} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

