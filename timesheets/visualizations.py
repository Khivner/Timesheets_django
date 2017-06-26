import django
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from projectmanager.models import Projects

#color projects
#size hours
def HoursPieChart(request):
	#import pdb; pdb.set_trace()
	project_names = [project.client +': '+ project.project_name for project in Projects.objects.filter(id__in=request.session['projects_select'])]
	project_totals = request.session['results']
	project_names = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(project_names, [100*x for x in project_totals])]
	
	explode = [0.01 for x in project_names]

	
	fig = Figure(figsize=(7,7))
	ax = fig.add_subplot(111)
	fig.patch.set_alpha(0.0)
	ax.pie(project_totals, shadow=False, startangle=90, explode=explode)
	ax.legend(labels=project_names, loc="best")
	ax.axis('equal')
	canvas=FigureCanvas(fig)
	response=django.http.HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response