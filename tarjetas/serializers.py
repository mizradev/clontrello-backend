from rest_framework import serializers

from tarjetas.models import Tarjetas

class TarjetaSerializer(serializers.ModelSerializer):
	"""docstring for TarjetaSerializer"""
	class Meta:
		model = Tarjeta
		fields = ['nombre', 'descripcion']