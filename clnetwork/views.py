from rest_framework import viewsets
from .models import CLNetwork
from .serializers import CLNetworkSerializer


class CLNetworkViewSet(viewsets.ModelViewSet):
    queryset = CLNetwork.objects.all()
    serializer_class = CLNetworkSerializer
