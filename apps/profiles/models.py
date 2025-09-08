from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', default='profile_photos/default.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'