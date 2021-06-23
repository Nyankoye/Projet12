from django.contrib.auth import models
from rest_framework import fields, serializers
from crm.models import User, Client, Contract, Event, Team


class SerializerUser(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','password2']
        extra_kwargs ={
            'password':{'write_only':True},
        }
    
    def save(self):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'les mots de passe doivent correspondre'})
        user.set_password(password)
        user.save()
        return user


class SerializerClient(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'



class SerializerContract(serializers.ModelSerializer):
    
    class Meta:
        model = Contract
        fields = ['status', 'amount', 'payment_due', 'client', 'user']


class SerializerEvent(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['attendees', 'note', 'client', 'event_date', 'user', 'contract']


