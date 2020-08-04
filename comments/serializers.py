from rest_framework import serializers

from comments.models import Comments
from users.serializers import BaseUserSerializer


class CommentsSerializer(serializers.ModelSerializer):
	comments = BaseUserSerializer(read_only=True)


class Meta:
	model = Comments
	fields = ['card', 'message', 'owner', 'creation_date']