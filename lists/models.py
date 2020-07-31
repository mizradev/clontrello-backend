from django.db import models

from boards.models import Board


class List(models.Model):
    name = models.CharField(max_length=50)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    creation_date = models.DateTimeField(auto_now_add=True)
    position = models.IntegerField(6)

    def __str__(self):
        return self.name
