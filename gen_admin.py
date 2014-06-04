def buildfile(modname, lstclassnames):
	output='''\
from django.contrib import admin
from %(modname)s.models import %(csv_classnames)s

classes=[%(csv_classnames)s]

for iterclass in classes:
	admin.site.register(iterclass)
''' % {'modname': modname, 'csv_classnames': ','.join(lstclassnames)}

	return output