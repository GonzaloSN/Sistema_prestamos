from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from users.forms import CreateForm, UpdateForm
from .tables import UserTable
from django_tables2 import SingleTableView
from django.db.models import Q
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import PermissionsRequiredMixin

# Create your views here.


# View para buscar y listar usuarios

class UserListView(PermissionsRequiredMixin, LoginRequiredMixin, SingleTableView):
    template_name = 'users/listar.html'
    table_class = UserTable
    paginate_by = 20
    required_permissions = ('auth.add_user',)

    def get_queryset(self):
        if self.request.GET.get('q', False):
            search = self.request.GET['q']
            qs = Q(username__icontains=search) | \
                 Q(first_name__icontains=search) | \
                 Q(last_name__icontains=search) | \
                 Q(email__icontains=search)

            return User.objects.filter(qs).filter(is_superuser=False).order_by('id')

        return User.objects.get_queryset().filter(is_superuser=False).order_by('id')

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


# View para registrar usuarios

class UserCreateView(PermissionsRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
	model = User
	template_name = "users/registrar.html"
	form_class = CreateForm
	success_message = 'Usuario creado exitosamente'
	success_url = reverse_lazy('usuario:listar')
	required_permissions = ('auth.add_user',)


# View para modificar usuarios 

class UserUpdateView(PermissionsRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	template_name = 'users/modificar.html'
	model = User
	form_class = UpdateForm
	success_url = reverse_lazy('usuario:listar')
	success_message = 'Usuario actualizado exitosamente'
	required_permissions = ('auth.change_user',)

	def get_object(self, queryset=None):
	    return User.objects.get(pk=self.kwargs['pk'])


# View para eliminar usuarios

class UserDeleteView(PermissionsRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
	template_name = 'users/eliminar.html'
	model = User
	success_url = reverse_lazy('usuario:listar')
	success_message = 'Usuario eliminado exitosamente'
	required_permissions = ('auth.delete_user',)

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(UserDeleteView, self).delete(request, *args, **kwargs)

