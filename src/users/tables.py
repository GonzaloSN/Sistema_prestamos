from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
import django_tables2 as tables


class UserTable(tables.Table):
    options = tables.Column(verbose_name=_('Opciones'), orderable=False, empty_values=(),
                            attrs={
                                'td': {'class': 'text-center'},
                                'th': {"class": "text-center col-md-2"}})

    class Meta:
        model = User
        template = 'django_tables2/bootstrap.html'
        exclude = ('password', 'last_login', 'is_staff', 'is_superuser')
        sequence = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser')

    def __init__(self, *args, **kwargs):
        super(UserTable, self).__init__(*args, **kwargs)
        self.edit_text = _('Modificar')
        self.delete_text = _('Eliminar')

    def render_options(self, value, record):
        return mark_safe(
            '''
            <a href="{0}" class="btn btn-sm btn-success tooltip-link"
                data-original-title="{1}">
                <i class="fa fa-pencil-square-o"></i> {1}
            </a>
            <a href="{2}" class="btn btn-sm btn-danger tooltip-link"
                data-original-title="{3}">
                <i class="fa fa-user-times"></i> {3}
            </a>
            '''.format(
                reverse_lazy('usuario:editar', kwargs={'pk': record.pk}),
                'Modificar',
                reverse_lazy('usuario:eliminar', kwargs={'pk': record.pk}),
                'Eliminar'
            )
        )