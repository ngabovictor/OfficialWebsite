from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from mainpage.models import services_all, staff, home_banner, services_banner, products
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^success$', views.success, name= 'index'),
    url(r'^send$', views.send_message, name= 'Sent'),
]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
