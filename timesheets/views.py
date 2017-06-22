from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import timesheet_entry_create, timesheet_query_form
from .models import Devs_Time_Reports
from django.db.models import Sum
import datetime
import projectmanager

def Check_Admin_Request(User):
	if "AdminUsers" in User.groups.all().values_list('name', flat=True):
		return True
	return False

@login_required(login_url='login')
def home(request):
	grouplist = [group.name for group in request.user.groups.all()]
	entrylist = Devs_Time_Reports.objects.all().filter(dev_ID_id=request.user.id)
	#import pdb; pdb.set_trace()
	return render(request, 'home.html', {'grouplist': grouplist, 'entrylist':entrylist})

@login_required(login_url='login')
def timesheet_entry(request):
	grouplist = [group.name for group in request.user.groups.all()]
	if request.method == "POST":
		form = timesheet_entry_create(request.POST)

		if form.is_valid():
			total_post_time = datetime.timedelta(hours=int(request.POST['time_spent_hours']), minutes=int(request.POST['time_spent_min']))
			timesheet = Devs_Time_Reports(
				dev_ID=request.user, 
				project_ID= projectmanager.models.Projects.objects.get(pk=request.POST['projectname']), 
				time_spent=total_post_time, 
				items_complete=request.POST['items_complete'])
			timesheet.save()
			return redirect('home')
	else:
		form = timesheet_entry_create()

	return render(request, 'timesheet_entry.html', {'form': form, 'grouplist':grouplist})


@login_required(login_url='login')
@user_passes_test(Check_Admin_Request, login_url='login')
def timesheet_query(request):
	grouplist = [group.name for group in request.user.groups.all()]
	if request.method == "POST":
		form = timesheet_query_form(request.POST)

		if form.is_valid():
			request.session['users_query'] = [name.username for name in form.cleaned_data['users_query']]
			request.session['projects_select'] = form.cleaned_data['projects_select']
			request.session['start_time_query'] = form.cleaned_data['start_time_query'].strftime('%m/%d/%Y')
			request.session['end_time_query'] = form.cleaned_data['end_time_query'].strftime('%m/%d/%Y')

			return redirect('query_results')
	else:
		form = timesheet_query_form()

	return render(request, 'timesheet_query.html', {'form': form, 'grouplist':grouplist})

@login_required(login_url='login')
@user_passes_test(Check_Admin_Request, login_url='login')
def query_results(request):
	grouplist = [group.name for group in request.user.groups.all()]
	results = Devs_Time_Reports.objects.all()

	if request.session['users_query'] != []:
		results = results.filter(dev_ID_id__username__in=request.session['users_query'])

		
	if request.session['projects_select'] != []:
		results = results.filter(project_ID_id__in=request.session['projects_select'])
	
	if request.session['start_time_query'] != None:
		results = results.filter(entry_date__gte=datetime.datetime.strptime(request.session['start_time_query'], '%m/%d/%Y'))

	if request.session['end_time_query'] != None:
		results = results.filter(entry_date__lte=datetime.datetime.strptime(request.session['end_time_query'], '%m/%d/%Y'))
	
	total_time = results.aggregate(Sum('time_spent'))
	total_items = results.aggregate(Sum('items_complete'))

	return render(request, 'query_results.html', {'results': results, 'total_time':total_time, 'total_items':total_items, 'grouplist':grouplist})#
