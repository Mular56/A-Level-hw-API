from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes'
    )

    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', ]
