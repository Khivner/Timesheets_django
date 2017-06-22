from django.db import models
from django.contrib.auth.models import User
import projectmanager

# Create your models here.
class Devs_Time_Reports(models.Model):
	dev_ID = models.ForeignKey(User)
	#project_name
	project_ID = models.ForeignKey('projectmanager.Projects')
	time_spent = models.DurationField(blank=False)
	items_complete = models.IntegerField(default=None, blank=True, null=True)
	entry_date = models.DateField(auto_now_add=True)

