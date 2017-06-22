from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Projects(models.Model):
	project_name = models.CharField(max_length=100, unique=True, blank=False)
	client = models.CharField(max_length=100, blank=False)
	date_created = models.DateTimeField(auto_now_add=True)