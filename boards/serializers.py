from rest_framework import serializers

from boards.models import Board
from users.serializers import BaseUserSerializer


class BoardSerializer(serializers.ModelSerializer):
    board = BaseUserSerializer(read_only=True)

    class Meta:
        model = Board
        fields = ['name', 'description', 'creation_date']
