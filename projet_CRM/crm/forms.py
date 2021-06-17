from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Client, User, Contract, Team, Event


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'team', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'team', 'is_superuser', 'is_active']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class ClientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(team__name='Equipe Vente')
        self.fields['user'].label = 'Commercial'

    class Meta:
        model = Client
        fields = '__all__'


class ContractForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(team__name='Equipe Vente')
        self.fields['user'].label = 'Commercial'

    payment_due = forms.DateTimeField(label='Echéance de payement',
                                      widget=forms.DateTimeInput(
                                          attrs={'type': 'datetime-local'}
                                      )
                                      )
    amount = forms.FloatField(label='Montant',
                              widget=forms.TextInput(
                                  attrs={'placeholder': '100.25'}
                              )
                              )

    class Meta:
        model = Contract
        fields = ['status', 'amount', 'payment_due', 'client', 'user']


class EventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(team__name='Equipe Support')
        self.fields['user'].label = 'Gérer par'

    event_date = forms.DateTimeField(label='Date Evenement',
                                     widget=forms.DateTimeInput(
                                         attrs={'type': 'datetime-local'}
                                     )
                                     )

    class Meta:
        model = Event
        fields = ['attendees', 'note', 'client', 'event_date', 'user', 'contract']
