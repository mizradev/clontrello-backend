from django.db import models

# Create your models here.
class Comments(models.Model):
	"""docstring for Comentarios"""
	card = models.ForeignKey('tarjetas', on_delete=models.CASCADE)
	message = models.TextField()
	owner = models.ForeignKey('usuarios', on_delete=models.CASCADE)
	creation_date = models.DateTimeField(auto_now_add=True)