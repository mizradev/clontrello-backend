from django.db import models

"""
Comentarios
	Tarjeta (Llave foránea)
	Mensaje (Texto)
	Dueño (Llave foránea)
	Fecha de creación (Fecha y hora)
"""

class Comentarios(models.Model):
	"""docstring for Comentarios"""
	tarjeta = models.ForeignKey('tarjetas', on_delete=models.CASCADE)
	mensaje = models.TextField()
	propietario = models.ForeignKey('usuarios', on_delete=models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now_add=True) 
	# def __init__(self, arg):
	# 	super(Comentarios, self).__init__()
	# 	self.arg = arg

