from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm, UserUpdateForm, ClientForm, ContractForm, EventForm
from .permissions import OnlyTeamManagement, OnlyOwnerOrSupport, OnlySaleOrManagementTeam, \
    OnlySaleOrManagementTeamCanDelete
from .models import User, Client, Contract, Event


# Create your views here.

class HelloView(LoginRequiredMixin, TemplateView):
    template_name = 'crm/index.html'


class UsersListView(LoginRequiredMixin, OnlyTeamManagement, ListView):
    model = User
    paginate_by = 5
    context_object_name = 'users'
    template_name = 'crm/users.html'


class UserProfileView(LoginRequiredMixin, OnlyTeamManagement, DetailView):
    model = User
    template_name = 'crm/profile.html'

    def get_object(self, queryset=None):
        return User.objects.get(id=self.kwargs.get("id"))


class UserLoggedProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'crm/logged_profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class UserCreateView(OnlyTeamManagement, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'crm/register.html'
    success_url = reverse_lazy('create_user')
    form_class = UserForm
    success_message = "Le compte à bient été créer"


class UserUpdateView(OnlyTeamManagement, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'crm/update_profile_id.html'
    success_url = reverse_lazy('users')
    success_message = "Votre profile a bient été modifié"

    def get_object(self, queryset=None):
        return User.objects.get(id=self.kwargs.get("id"))


class UserDeleteView(OnlyTeamManagement, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users')
    success_message = "le compte a bien été supprimé"

    def get_object(self, queryset=None):
        return User.objects.get(id=self.kwargs.get("id"))


class UpdateProfileView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'crm/update_profile.html'
    success_url = reverse_lazy('update_profile')
    success_message = "Votre profile à bient été modifié"

    def get_object(self, queryset=None):
        return self.request.user


class ChangePasswordView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'crm/password_change.html'
    success_url = reverse_lazy('password_success')
    success_message = "Votre mot de passe à bien été modifié"


class PassWordSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'crm/password_success.html'


class ClientCreateView(OnlySaleOrManagementTeam, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ClientForm
    template_name = 'crm/create_client.html'
    success_url = reverse_lazy('create_client')
    success_message = "Les informations du client sont enregistrées"


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = 'clients'
    paginate_by = 5
    template_name = 'crm/clients.html'


class ClientUpdateView(LoginRequiredMixin, OnlyOwnerOrSupport, SuccessMessageMixin, UpdateView):
    form_class = ClientForm
    template_name = 'crm/update_client.html'
    success_url = reverse_lazy('clients')
    success_message = "Les informations du client ont été modifiées avec succès"

    def get_object(self, queryset=None):
        return Client.objects.get(id=self.kwargs.get("id"))


class ClientDeleteView(SuccessMessageMixin, OnlyOwnerOrSupport, LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients')
    success_message = "Les informations du client ont été supprimées"

    def get_object(self, queryset=None):
        return Client.objects.get(id=self.kwargs.get("id"))


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'crm/client_detail.html'
    context_object_name = 'client'

    def get_object(self, queryset=None):
        return Client.objects.get(id=self.kwargs.get("id"))


class ContractCreateView(OnlySaleOrManagementTeam, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ContractForm
    template_name = 'crm/create_contract.html'
    success_url = reverse_lazy('create_contract')
    success_message = "Le contrat à été enregistrée"


class ContractListView(LoginRequiredMixin, ListView):
    model = Contract
    context_object_name = 'contracts'
    template_name = 'crm/contracts.html'
    paginate_by = 5


class ContractUpdateView(OnlySaleOrManagementTeam, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = ContractForm
    template_name = 'crm/update_contract.html'
    success_url = reverse_lazy('contracts')
    success_message = "Modifications Réussies"

    def get_object(self, queryset=None):
        return Contract.objects.get(id=self.kwargs.get("id"))


class ContractDeleteView(OnlySaleOrManagementTeam, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Contract
    success_url = reverse_lazy('contracts')
    success_message = "Le contrat à été Supprimé"

    def get_object(self, queryset=None):
        return Contract.objects.get(id=self.kwargs.get("id"))


class ContractDetailView(LoginRequiredMixin, DetailView):
    model = Contract
    template_name = 'crm/contract_detail.html'
    context_object_name = 'contract'

    def get_object(self, queryset=None):
        return Contract.objects.get(id=self.kwargs.get("id"))


class EventCreateView(OnlySaleOrManagementTeam, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = EventForm
    template_name = 'crm/create_event.html'
    success_url = reverse_lazy('create_event')
    success_message = "L'evenement à été créer"


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'crm/events.html'
    paginate_by = 5
    context_object_name = 'events'

    def get_queryset(self):
        if self.request.user.team.name == 'Equipe Support':
            return Event.objects.filter(user=self.request.user)
        else:
            return Event.objects.all()


class EventUpdateView(SuccessMessageMixin, OnlyOwnerOrSupport, LoginRequiredMixin, UpdateView):
    form_class = EventForm
    template_name = 'crm/update_event.html'
    success_url = reverse_lazy('events')
    success_message = "Modifications Réussies"

    def get_object(self, queryset=None):
        return Event.objects.get(id=self.kwargs.get("id"))


class EventDeleteView(SuccessMessageMixin, OnlySaleOrManagementTeamCanDelete, LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events')
    success_message = "Suppression  Réussies"

    def get_object(self, queryset=None):
        return Event.objects.get(id=self.kwargs.get("id"))


class EventDetailView(SuccessMessageMixin, LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'crm/event_detail.html'

    def get_object(self, queryset=None):
        return Event.objects.get(id=self.kwargs.get("id"))
