from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=30)
    content = models.CharField(max_length=150)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)

    def __str__(self):
        return f"Note from {self.author.username} @{self.author.department} - {self.created_at.strftime("%A %d. %B %Y")}"

