from django.db import models
from django.contrib.auth.models import User
import os

def avatar_upload_path(instance, filename):
    return f"avatars/user_{instance.user.id}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to=avatar_upload_path, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    # Delete avatar file from storage when profile is deleted
    def delete(self, *args, **kwargs):
        if self.avatar and os.path.isfile(self.avatar.path):
            os.remove(self.avatar.path)
        super().delete(*args, **kwargs)
