from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .models import Projects
from .forms import MakeProjectForm

def Check_Admin_Request(User):
	if "AdminUsers" in User.groups.all().values_list('name', flat=True):
		return True
	return False

# Create your views here.
@login_required(login_url='login')
@user_passes_test(Check_Admin_Request, login_url='login')
def create_project(request):
	grouplist = [group.name for group in request.user.groups.all()]
	if request.method == "POST":
		form = MakeProjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = MakeProjectForm()
	return render(request, 'create_project.html', {'form':form, 'grouplist':grouplist})