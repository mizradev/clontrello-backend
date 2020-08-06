from django.db import models

from lists.models import List
from users.models import User


class Card(models.Model):
	name = models.CharField(max_length=100)
	list = models.ForeignKey(List, on_delete=models.CASCADE) #(Llave foránea)
	description = models.TextField(max_length=100)
	members = models.ManyToManyField(User)
	owner = models.ForeignKey(User, on_delete=models.CASCADE) #(Llave foránea)
	creation_date = models.DateTimeField(auto_now_add=True)
	due_date = models.DateTimeField(null=True)

	def __str__(self):
		return self.name

