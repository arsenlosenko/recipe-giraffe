from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model


def recipe_image_path(instance, filename):
    return '{}/{}'.format(instance.recipe_id, uuid4())


class Recipe(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "{} by {}".format(self.title, self.user.username)


class RecipeImage(models.Model):
    image = models.ImageField(upload_to=recipe_image_path)
    uploaded = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
