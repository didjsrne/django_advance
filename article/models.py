from tkinter import CASCADE
from django.db import models
# from django.contrib.auth.models import User  # 1번
from django.contrib.auth import get_user_model  # 2번

class Article(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)