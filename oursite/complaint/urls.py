from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^details/(?P<id>\d+)', views.details, name='details'),
	url(r'^department/(?P<id>\d+)', views.department, name="department"),
	url(r'^new/', views.new_compl, name="new_compl"),
	url(r'^new_compl/', views.new_compl_form, name="new_compl_form")
]