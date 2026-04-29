from django.db import models
from django.contrib.auth.models import User



class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} | {self.name}"
    
class Test(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title