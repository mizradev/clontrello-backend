from rest_framework import serializers

from cards.models import Cards

class CardsSerializer(serializers.ModelSerializer):
	"""docstring for TarjetaSerializer"""
	class Meta:
		model = Cards
		fields = ['name', 'description']