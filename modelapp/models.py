from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        default="",
    )
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    photo_url = models.CharField(max_length=2000, null=True, blank=True, default="")


class User(models.Model):
    first_name = models.CharField(
        max_length=100,
        null=False,
    )
