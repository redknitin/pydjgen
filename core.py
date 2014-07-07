import os, re
#import gen_urls, gen_views

#modeldirname contains the name of the immediate parent directory (not full path; only its name)
modeldirname = os.path.dirname(os.path.realpath(__file__)).split(os.sep)[-1]  #TODO: Use models.__file__ instead of __file__ of the current file

cre = re.compile(r'class +(.*) *'+re.escape('('))
modelfile = open('models.py', 'r')

lstclassnames = []

for line in modelfile:
	cap = cre.match(line)
	if not cap is None:
		classname = cap.group(1)
		if not classname.endswith('Base'): #ignore base classes
			lstclassnames.append(classname)

#if len(lstclassnames)==0:
#	pass

modelfile.close()

#modname='oradb'
#lstclassnames=['Emp', 'Dept']

#content_urls=gen_urls.buildfile(modeldirname, lstclassnames)
#print(content_urls)
#content_views=gen_views.buildfile(modeldirname, lstclassnames)
#print(content_views)
#content_forms=gen_forms.buildfile(modeldirname, lstclassnames)
#print(content_forms)
#content_admin=gen_admin.buildfile(modeldirname, lstclassnames)
#print(content_admin)
