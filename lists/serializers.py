from boards import serializers
from lists.models import List
from users.serializers import BaseUserSerializer


class ListSerializer(serializers.ModelSerializer):
    User = BaseUserSerializer(read_only=True)

    class Meta:
        model = List
        fields = ['name', 'board', 'date_creation', 'position']
