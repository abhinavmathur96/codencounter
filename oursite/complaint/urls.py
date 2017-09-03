from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^details/(?P<id>\d+)', views.details, name='details'),
	url(r'^department/login/$', views.dept_login, name="dept_login"),
	url(r'^department/(?P<id>\d+)', views.department_id, name="department"),
	url(r'^department/detail/(?P<id>\d+)', views.details, name="department_detail"),
	url(r'^new/', views.new_compl, name="new_compl"),
	url(r'^thanks/',views.thanks, name = "thanks"),
	url(r'^complete/(?P<dept_id>\d+)/(?P<id>\d+)',views.complete,name='complete')
]