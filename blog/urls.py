from django.conf.urls import url
from blog import views, login

urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^home/$', views.home, name='home'),
]