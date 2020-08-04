from rest_framework import serializers

from cards.models import Cards
from users.serializers import BaseUserSerializer


class CardsSerializer(serializers.ModelSerializer):
	cards = BaseUserSerializer(read_only=True)


class Meta:
	model = Cards
	fields = ['name', 'list', 'description', 'members', 'owner', 'creation_date', 'due_date']



