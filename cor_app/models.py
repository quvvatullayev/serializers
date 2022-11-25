from django.db import models
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.username

class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    status = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')

    def __str__(self) -> str:
        return self.name