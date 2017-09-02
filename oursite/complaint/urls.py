from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index")
	url(r'^details/(?P<id>\d+)', views.details, name='details')
	url(r'^department/(?P<id>\d+)', views.department, name="department")
]