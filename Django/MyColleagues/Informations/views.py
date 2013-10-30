from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from Informations.models import Information
from Informations.forms import AddForm

def display_information(request):
	information_list = Information.objects.all()
	return render_to_response('Information.html', {'information_list': information_list})

def add(request):
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			p = Information(name=cd['name'], sex=cd['sex'],number=cd['number'],popo=cd['popo'],phone=cd['phone'])
			p.save()
			return HttpResponseRedirect('/information/')
	else:
		form = AddForm(
			#initial={'subject': 'I love your site!'}
		)
	return render_to_response('add_form.html', {'form': form}, RequestContext(request))
