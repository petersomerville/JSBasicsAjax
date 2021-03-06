from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
