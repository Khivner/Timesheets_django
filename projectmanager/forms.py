from django import forms
from .models import Projects
from django.contrib.auth.models import Group, User
from django.forms import ModelChoiceField

class MakeProjectForm(forms.ModelForm):

	class Meta:
		model = Projects
		fields = ('project_name', 'client',)