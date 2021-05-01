from django.urls import path
from . import views

urlpatterns = [
	path('', views.post, name='post'),
	path('about', views.about, name='about')
]
