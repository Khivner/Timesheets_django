from django import forms
from .models import Devs_Time_Reports
from projectmanager.models import Projects
from django.contrib.auth.models import Group, User
from django.forms import ModelChoiceField
import projectmanager
import datetime

project_query = [(project.pk, project.client +': '+project.project_name) for project in Projects.objects.all()]

class timesheet_entry_create(forms.Form):
	projectname = forms.ChoiceField(choices=project_query, label='Project')
	time_spent_hours = forms.IntegerField(label='Hours')
	time_spent_min = forms.IntegerField(label='Minutes')
	items_complete = forms.IntegerField()

class timesheet_query_form(forms.Form):
	users_query = forms.ModelMultipleChoiceField(queryset=User.objects.all().order_by('username'), label='Users')
	projects_select = forms.MultipleChoiceField(choices=project_query, label='Users')
	start_time_query = forms.DateField(initial=datetime.date.today().strftime('%m/%d/%Y'))
	end_time_query = forms.DateField(initial=datetime.date.today().strftime('%m/%d/%Y'))

	def __init__(self, *args, **kwargs):
		super(timesheet_query_form, self).__init__(*args, **kwargs)

		for key in self.fields:
			self.fields[key].required = False