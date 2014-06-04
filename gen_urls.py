def buildfile(modname, lstclassnames):
	output='''\
from %(modname)s import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	
#	url(r'^$', views.home),

''' % {'modname': modname}

	for classname in lstclassnames:
		lc_classname = classname.lower()

		output+='''\
	url(r'^%(lc_classname)s/edit/(?P<id>\d+)$', views.%(lc_classname)s_edit, name='%(lc_classname)s_edit'),
	url(r'^%(lc_classname)s/index$', views.%(lc_classname)s_home, name='%(lc_classname)s_list'),
	url(r'^%(lc_classname)s$', views.%(lc_classname)s_home, name='%(lc_classname)s_list'),
	url(r'^%(lc_classname)s/delete/(?P<id>\d+)$', views.%(lc_classname)s_delete, name='%(lc_classname)s_delete'),
		
''' % {'lc_classname': lc_classname}

	output+='''\
)
'''

	return output