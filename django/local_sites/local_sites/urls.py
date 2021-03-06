"""local_sites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from local_sites import views as local_views



urlpatterns = [
    # admin content
	path('admin/', admin.site.urls),
	url(r'^home/$',local_views.home,name ='home'),		
	url(r'^login/$',auth_views.login, {'template_name': 'login.html'}, name ='login'),
	url(r'^singup/$',local_views.singup, name ='singup'),
	url(r'^logout/$',auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
	
	
	
	
	# single apps pointers
	path('poc_teaching/',include('poc_teaching.urls')),
	path('^$', RedirectView.as_view(url='/poc_teaching/',permanent=True)),
	
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
