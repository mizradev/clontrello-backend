from django.db import models

from users.models import User
from cards.models import Cards

# Create your models here.
class Comments(models.Model):
	"""docstring for Comentarios"""
	card = models.ForeignKey(Cards, on_delete=models.CASCADE)
	message = models.TextField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	creation_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
        return self.name