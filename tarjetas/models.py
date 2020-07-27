from django.db import models

"""
Tarjetas
	Nombre (Texto)
	Lista (Llave foránea)
	Descripción (texto)
	Miembros (Muchos a muchos)
	Dueño (Llave foránea)
	Fecha de creación (Fecha y hora)
	Fecha de vencimiento (Fecha y hora)
	Posición (Entero)

"""
class Tarjetas(models.Model):
	"""docstring for Tarjetas"""
	nombre = models.CharField(max_length=100)
	lista = models.ForeignKey('listas', on_delete=models.CASCADE) #(Llave foránea)
	descripcion = models.TextField()
	miembros = models.ManyToManyField('usuarios')
	propietario = models.ForeignKey('usuarios', on_delete=models.CASCADE) #(Llave foránea)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_vencimiento = models.DateTimeField(null=True)
	
	# def __init__(self, arg):
	# 	super(Tarjetas, self).__init__()
	# 	self.arg = arg
	# 	