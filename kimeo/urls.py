"""kimeo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from kimeo import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from KimeoApp import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^home', views.home),
    url(r'^about', views.about),
    url(r'^portfolio', views.portfolio),
    url(r'^actions', views.actions),
    url(r'^control', views.control),
    url(r'^movement', views.movement),
    url(r'^message', views.message),
    url(r'^monitoring', views.monitoring),
    url(r'^contact', views.contact),
    url(r'mail',views.mail),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/messages/$', views.MessageList.as_view()),
    url(r'^api/messages/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view()),
    url(r'^api/movements/$', views.MovementList.as_view()),
    url(r'^api/movements/(?P<pk>[0-9]+)/$', views.MovementDetail.as_view()),
    url(r'^api/lights/$', views.LightList.as_view()),
    url(r'^api/lights/(?P<pk>[0-9]+)/$', views.LightDetail.as_view()),
    url(r'^api/sounds/$', views.SoundList.as_view()),
    url(r'^api/sounds/(?P<pk>[0-9]+)/$', views.SoundDetail.as_view()),
    url(r'^api/screens/$', views.ScreentList.as_view()),
    url(r'^api/screens/(?P<pk>[0-9]+)/$', views.ScreenDetail.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()