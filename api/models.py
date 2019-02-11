from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "{} by {}".format(self.title, self.user.username)
