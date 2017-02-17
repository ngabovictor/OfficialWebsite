from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from mainpage.models import services_all, staff, home_banner, services_banner, products
from custommail.models import mailbox
from datetime import datetime
from django.utils import timezone

# Create your views here.
def index(request):
	context_dict = {}

	context_dict['home_banner_items'] = home_banner.objects.all()
	context_dict['staff'] = staff.objects.all()
	context_dict['services'] = services_all.objects.all()
	context_dict['services_banner_items'] = services_banner.objects.all()
	context_dict['products_items'] = products.objects.all()
	return render(request, 'home.html', context_dict)

def success(request):
	context_dict = {}

	context_dict['home_banner_items'] = home_banner.objects.all()
	context_dict['staff'] = staff.objects.all()
	context_dict['services'] = services_all.objects.all()
	context_dict['services_banner_items'] = services_banner.objects.all()
	context_dict['products_items'] = products.objects.all()
	return render(request, 'success.html', context_dict)

def send_message(request):
	name = request.POST['name']
	email = request.POST['email']
	message = request.POST['message']
	classifications = 'Unread'
	date = datetime.today()

	mailbox.objects.create(
		name = name,
		email = email,
		message = message,
		classifications = classifications,
		date = date,
		)
	return HttpResponseRedirect('success')


