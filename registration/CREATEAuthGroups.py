from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
import projectmanager

admin, created = Group.objects.get_or_create(name='AdminUsers')
# Code to add permission to group ???
ct = ContentType.objects.get_for_model(projectmanager.Projects)

# Now what - Say I want to add 'Can add project' permission to new_group?
permission = Permission.objects.create(codename='can_create_project',
                                   name='Can add project',
                                   content_type=ct)
admin.permissions.add(permission)