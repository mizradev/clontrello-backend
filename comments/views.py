from django.shortcuts import render

from rest_framework import viewsets

from comments.models import Comments
from comments.serializers import CommentsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
	class Meta:
		queryset = Comments.objects.all()
		serializer_class = CommentsSerializer 

