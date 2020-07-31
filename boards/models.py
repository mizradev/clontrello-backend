from django.db import models

# Create your models here.
from users.models import User


class Board(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE(), related_name='boards')
    favorite = models.ManyToManyRel(User)
    visibility = models.TextChoices()
    members = models.ManyToManyRel(User)

    def __str__(self):
        return self.name
