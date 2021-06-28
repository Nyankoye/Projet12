from django.urls import path, include, re_path
from api import views as api_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clients', api_view.ClientView, basename='clients')
router.register('contracts', api_view.ContractView, basename='contracts')
router.register('events', api_view.EventView, basename='events')

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^login/', include('rest_framework.urls', namespace='auth'))
]
