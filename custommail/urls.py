from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from custommail.models import mailbox
from custommail import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.login, name= 'login'),
	url(r'^auth', views.auth_view, name = 'Auth'),
	url(r'^invalid', views.invalid_login, name = 'invalid'),
    url(r'^messages', views.messages, name= 'messages'),
    url(r'^unread', views.unread, name= 'unread'),
    url(r'^read', views.read, name= 'read'),
    url(r'^login', views.login, name= 'login'),
    url(r'^logout', views.logout, name= 'login'),
    url(r'^0(?P<message_id>\d+)', views.message_view, name= 'message_view'),

]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)