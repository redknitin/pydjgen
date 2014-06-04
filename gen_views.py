def buildfile(modname, lstclassnames):
	output='''\
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

def home(request):
	return HttpResponse('Home page under construction', mimetype='text/plain')

'''

	for classname in lstclassnames:
		output+='''\
from %(modname)s.forms import %(classname)sForm
from %(modname)s.models import %(classname)s

def %(lc_classname)s_edit(request, id="0"):
	id=int(id)
	if request.method=="GET":
		if id>0:
			form=%(classname)sForm(instance=%(classname)s.objects.get(id=id))
		else:
			form=%(classname)sForm()
		return render(request, 'common_edit.html', {'form': form})
	else:
		if id>0:
			form=%(classname)sForm(request.POST, instance=%(classname)s.objects.get(id=id))
		else:
			form=%(classname)sForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('%(lc_classname)s_list'))
		else:
			return render(request, 'common_edit.html', {'form': form})

def %(lc_classname)s_home(request):
	data=%(classname)s.objects.all()
	return render(request, '%(lc_classname)s_list.html', {'data': data})

def %(lc_classname)s_delete(request, id):
	id=int(id)
	instance=%(classname)s.objects.get(id=id)
	instance.delete()	
	return HttpResponseRedirect(reverse('%(lc_classname)s_list'))

''' % {'modname': modname, 'classname': classname, 'lc_classname': classname.lower()}

	return output