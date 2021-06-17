from django.core.exceptions import PermissionDenied


class OnlyTeamManagement:
    """
        Cette classe nous permet de n'autoriser que les membre de l'equipe Gestion
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.team.name == 'Equipe Gestion':
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class OnlyOwnerOrSupport:
    """
        Cette classe nous permet de n'autoriser que les utilisateurs
    """

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class OnlySaleOrManagementTeam:
    """
        Cette classe nous permet de n'autoriser que les membre de l'equipe Vente et Gestion
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.team.name == 'Equipe Vente' or request.user.team.name == 'Equipe Gestion':
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class OnlySaleOrManagementTeamCanDelete:
    """
        Cette classe nous permet de n'autoriser que les membre de l'equipe Vente et Gestion
    """

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.contract.user != self.request.user or obj.user.team.name == 'Equipe Gestion':
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
