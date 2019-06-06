from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator


class PermissionsRequiredMixin(object):
    required_permissions = ()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms(self.required_permissions):
            messages.error(request,
                           'No tienes los permisos necesarios para realizar la operacion requerida.')
            raise PermissionDenied
        return super(PermissionsRequiredMixin, self).dispatch(request, *args, **kwargs)