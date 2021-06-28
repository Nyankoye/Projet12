from rest_framework import viewsets, permissions
from rest_framework import filters as filter
from django_filters import rest_framework as filters
from .serialisers import SerializerClient, SerializerContract, SerializerEvent
from crm.models import Client, Contract, Event
from .permissions import OnlyOwnerOrManagementTeam, AllowSupportManagementAndSale


# Create your views here.

class ClientFilter(filters.FilterSet):
    class Meta:
        model = Client
        fields = {
            'company_name': ['icontains'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'date_created': ['iexact', 'lte', 'gte']
        }


class ContractFilter(filters.FilterSet):
    status = filters.BooleanFilter()

    class Meta:
        model = Contract
        fields = {
            'date_created': ['iexact', 'lte', 'gte']
        }


class EventFilter(filters.FilterSet):
    class Meta:
        model = Event
        fields = {
            'attendees': ['iexact', 'lte', 'gte'],
            'date_created': ['iexact', 'lte', 'gte']
        }


class ClientView(viewsets.ModelViewSet):
    serializer_class = SerializerClient
    permission_classes = (permissions.IsAuthenticated, OnlyOwnerOrManagementTeam,)
    filterset_class = ClientFilter

    def get_queryset(self):
        return Client.objects.all().order_by('-date_updated')


class ContractView(viewsets.ModelViewSet):
    serializer_class = SerializerContract
    permission_classes = (permissions.IsAuthenticated, OnlyOwnerOrManagementTeam,)
    filterset_class = ContractFilter

    def get_queryset(self):
        return Contract.objects.all().order_by('-date_updated')


class EventView(viewsets.ModelViewSet):
    serializer_class = SerializerEvent
    permission_classes = (permissions.IsAuthenticated, AllowSupportManagementAndSale,)
    filterset_class = EventFilter

    def get_queryset(self):
        return Event.objects.all().order_by('-date_updated')
