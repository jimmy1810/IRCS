from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
	url(r'^$',views.index,name = 'index'),

	path('beqas/',views.beqas_form),
	path('beqassearch/',views.searchid),
	path('beqascycle/',views.searchby),
]
