from django.db import models

class Cards(models.Model):
	name = models.CharField(max_length=100)
	list = models.ForeignKey('listas', on_delete=models.CASCADE) #(Llave foránea)
	description = models.TextField()
	members = models.ManyToManyField('usuarios')
	owner = models.ForeignKey('usuarios', on_delete=models.CASCADE) #(Llave foránea)
	creation_date = models.DateTimeField(auto_now_add=True)
	due_date = models.DateTimeField(null=True)

