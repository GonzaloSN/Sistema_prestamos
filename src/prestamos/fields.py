from django.conf import settings

from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget
from django.contrib.auth.models import User


class UserSelectWidget(ModelSelect2Widget):
    model = User
    search_fields = [
        'username__icontains'
    ]