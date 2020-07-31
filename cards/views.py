from rest_framework import viewsets

from cards.models import Cards
from cards.serializers import CardsSerializer


class CardsViewSet(viewsets.ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
