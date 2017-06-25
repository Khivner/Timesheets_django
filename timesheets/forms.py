from django import forms
from .models import Devs_Time_Reports
from projectmanager.models import Projects
from django.contrib.auth.models import Group, User
from django.forms import ModelChoiceField
import datetime


class timesheet_entry_create(forms.Form):
	projectname = forms.ChoiceField(label='Project')
	time_spent_hours = forms.IntegerField(label='Hours')
	time_spent_min = forms.IntegerField(label='Minutes')
	items_complete = forms.IntegerField(required=False)

	def __init__(self, *args, **kwargs):
		#import pdb; pdb.set_trace()
		self.project_choices = kwargs.pop('project_choices')
		super(timesheet_entry_create, self).__init__(*args,**kwargs)
		self.fields['projectname'].choices = self.project_choices


class timesheet_query_form(forms.Form):
	users_query = forms.ModelMultipleChoiceField(queryset=User.objects.all().order_by('username'), label='Users')
	projects_select = forms.MultipleChoiceField(label='Projects')
	start_time_query = forms.DateField(initial=datetime.date.today().strftime('%m/%d/%Y'))
	end_time_query = forms.DateField(initial=datetime.date.today().strftime('%m/%d/%Y'))

	def __init__(self, *args, **kwargs):
		self.project_choices = kwargs.pop('project_choices')
		super(timesheet_query_form, self).__init__(*args, **kwargs)
		self.fields['projects_select'].choices = self.project_choices


		for key in self.fields:
			self.fields[key].required = False