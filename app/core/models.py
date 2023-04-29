from django.db import models # noqa

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)