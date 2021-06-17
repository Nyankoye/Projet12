from django.contrib import admin
from .models import Team, User, Client, Contract, Event


# Register your models here.

class UserInlines(admin.TabularInline):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser', ]
    extra = 0


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [UserInlines, ]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
