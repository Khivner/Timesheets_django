from django.conf.urls import url
from . import views

urlpatterns = [
	    url(r'^$', views.home, name='home'),
	    url(r'^timesheet_entry/', views.timesheet_entry, name='timesheet_entry'),
	    url(r'^timesheet_query/', views.timesheet_query, name='timesheet_query'),
	    url(r'^query_results/', views.query_results, name='query_results'),
]