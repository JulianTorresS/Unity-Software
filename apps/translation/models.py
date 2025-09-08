from django.db import models
from django.contrib.auth.models import User

class Translation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_text = models.TextField()
    translated_text = models.TextField()
    target_language = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Traducción de {self.user.username} ({self.created_at.strftime("%Y-%m-%d")})'