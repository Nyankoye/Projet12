from rest_framework.permissions import BasePermission
from rest_framework import permissions


class OnlyOwnerOrManagementTeam(BasePermission):
    """
        les membre de l'équipe vente ont accès en lecture seule à tous les clients.
         Un droit de modification/d'accès pour tous les clients dont ils sont responsables,
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.team.name == 'Equipe Gestion' or request.user.team.name == 'Equipe Vente':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.team.name == 'Equipe Gestion':
            return True
        return obj.user == request.user


class AllowSupportManagementAndSale(BasePermission):
    """
        les membre de l'équipe vente ont accès en lecture seule à tous les clients.
         Un droit de modification/d'accès pour tous les clients dont ils sont responsables,
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.team.name == 'Equipe Gestion' or request.user.team.name == 'Equipe Vente':
            return True
        elif request.user.team.name == 'Equipe Support' and request.method == 'PUT':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.team.name == 'Equipe Gestion':
            return True
        elif obj.contract.user == request.user:
            return True
        return obj.user == request.user
