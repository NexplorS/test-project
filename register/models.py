from django.db import models
from django.conf import settings
from django.db import models
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    work = models.CharField(max_length=20)
    hobby = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
