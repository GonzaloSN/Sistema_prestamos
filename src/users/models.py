from django.contrib.auth.models import Group
from django.db import models


Group.add_to_class('description', models.CharField(max_length=180, null=True, blank=True))