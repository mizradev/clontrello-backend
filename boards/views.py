from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from boards.models import Board
from boards.serializers import BoardSerializer


class BoardsViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
