from django.shortcuts import render
from rest_framework import viewsets

from lists.models import List
from lists.serializers import ListSerializer


class ListsViewSet(viewsets.ModelViewSet):
    class Meta:
        queryset = List.objects.all()
        serializer_class = ListSerializer
