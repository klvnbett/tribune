from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views 
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'',include('news.urls')),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^logout/$', views.LogoutView, {"next_page": ''}), 
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
]