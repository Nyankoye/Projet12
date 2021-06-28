from django.urls import path, include, re_path
from api import views as api_view
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register('clients', api_view.ClientView, basename='clients')
router.register('contracts', api_view.ContractView, basename='contracts')
router.register('events', api_view.EventView, basename='events')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
