from django.urls import path
from . import views

urlpatterns = [
	path('', views.post, name='post'),
	path('about', views.about, name='about'),
	path('postapp/login/', views.user_login, name='user_login'),
	path('postapp/register/', views.register, name='register')
]
