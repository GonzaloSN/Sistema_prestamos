from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Form para crear usuarios

class CreateForm(UserCreationForm):
    first_name = forms.CharField(label='Primer nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput,
        help_text='Requerido ingrese un email valido',
        required=True
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")

        if not extension == "com" and not extension == "cl":
            raise forms.ValidationError("Solo se aceptan correos con extension .COM o .CL ")

        return email


    groups = forms.ModelMultipleChoiceField(
        label='Grupos',
        widget=forms.CheckboxSelectMultiple,
        queryset=Group.objects.all(),
        required=False,
    )



    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if not commit:
            return user

        user.save()
        user.groups = self.cleaned_data['groups']
        return user

# Form para modificar usuarios

class UpdateForm(forms.ModelForm):
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput,
        help_text='Requerido ingrese un email valido',
        required=True
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")

        if not extension == "com" and not extension == "cl":
            raise forms.ValidationError("Solo se aceptan correos con extension .COM o .CL ")

        return email




    groups = forms.ModelMultipleChoiceField(
        label='Grupos',
        widget=forms.CheckboxSelectMultiple,
        queryset=Group.objects.all(),
        required=False,
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'groups')

