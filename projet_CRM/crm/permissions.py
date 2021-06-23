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


class OnlyOwnerOrManagementTeam:
    """
        Cette classe nous permet de n'autoriser que la personne qui à créer
    """

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.team.name == 'Equipe Gestion':
            return super().dispatch(request, *args, **kwargs)
        elif obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class OnlyCreatedByAndSupport:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.team.name == 'Equipe Gestion':
            return super().dispatch(request, *args, **kwargs)
        elif obj.contract.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        elif obj.user != self.request.user:
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


class OnlyOwnerOrManagementTeamCanDelete:
    """
        Cette classe nous permet de n'autoriser que le membre de l'equipe Vente qui à créer, tous les membre de l'equipe
        Gestion  et la personne de l'équipe support assignée.
    """

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user.team.name == 'Equipe Gestion':
            return super().dispatch(request, *args, **kwargs)
        elif obj.contract.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
