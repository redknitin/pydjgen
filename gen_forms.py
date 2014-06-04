def buildfile(modname, lstclassnames):
	output='''\
from django.forms import ModelForm

class BaseForm(ModelForm):
	required_css_class='required'
	class Meta:
		abstract=True

'''

	for classname in lstclassnames:
		output+='''\
from %(modname)s.models import %(classname)s

class %(classname)sForm(BaseForm):
	class Meta:
		model=%(classname)s

''' % {'modname': modname, 'classname': classname}

	return output