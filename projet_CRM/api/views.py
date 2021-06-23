from rest_framework import viewsets, permissions
from .serialisers import SerializerClient, SerializerContract, SerializerEvent
from crm.models import Client, Contract, Event

# Create your views here.


class ClientView(viewsets.ModelViewSet):
    serializer_class = SerializerClient
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Client.objects.all().order_by('-date_updated')

class ContractView(viewsets.ModelViewSet):
    serializer_class = SerializerContract
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Contract.objects.all().order_by('-date_updated')


class EventView(viewsets.ModelViewSet):
    serializer_class = SerializerEvent
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Event.objects.all().order_by('-date_updated')