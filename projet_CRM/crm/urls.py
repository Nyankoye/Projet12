from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HelloView, UserCreateView, UpdateProfileView, ChangePasswordView, PassWordSuccessView, \
    UsersListView, UserProfileView, UserUpdateView, UserDeleteView, UserLoggedProfileView, ClientCreateView,\
    ClientListView, ClientUpdateView, ClientDeleteView, ClientDetailView, ContractCreateView, ContractListView,\
    ContractUpdateView, ContractDeleteView, ContractDetailView, EventCreateView, EventListView, EventUpdateView,\
    EventDeleteView, EventDetailView

urlpatterns = [
    path('', HelloView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='crm/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='crm/logout.html'), name='logout'),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
    path('password_success/', PassWordSuccessView.as_view(), name='password_success'),
    path('users/', UsersListView.as_view(), name='users'),
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('update_profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/<int:id>', UserProfileView.as_view(), name='profile_detail'),
    path('update_profile/<int:id>/', UserUpdateView.as_view(), name='update_profile_id'),
    path('delete_user/<int:id>/', UserDeleteView.as_view(), name='delete_user'),
    path('profile', UserLoggedProfileView.as_view(), name='profile'),
    path('create_client', ClientCreateView.as_view(), name='create_client'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients_update/<int:id>/', ClientUpdateView.as_view(), name='clients_update'),
    path('clients_delete/<int:id>/', ClientDeleteView.as_view(), name='clients_delete'),
    path('clients_detail/<int:id>/', ClientDetailView.as_view(), name='clients_detail'),
    path('contracts/', ContractListView.as_view(), name='contracts'),
    path('create_contract/', ContractCreateView.as_view(), name='create_contract'),
    path('contract_update/<int:id>/', ContractUpdateView.as_view(), name='update_contract'),
    path('delete_contract/<int:id>/', ContractDeleteView.as_view(), name='delete_contract'),
    path('detail_contract/<int:id>/', ContractDetailView.as_view(), name='detail_contract'),
    path('create_event/', EventCreateView.as_view(), name='create_event'),
    path('events/', EventListView.as_view(), name='events'),
    path('update_event/<int:id>/', EventUpdateView.as_view(), name='update_event'),
    path('delete_event/<int:id>/', EventDeleteView.as_view(), name='delete_event'),
    path('event_detail/<int:id>/', EventDetailView.as_view(), name='event_detail'),
]
