from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from custommail.models import mailbox
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
# Create your views here.
@login_required(login_url="login")
def messages(request):
  # Book.objects.filter(publisher__name='BaloneyPress').count()

	context_dict_all = {}

	context_dict_all['inbox'] = mailbox.objects.all()
	context_dict_all['all_messages'] = mailbox.objects.all().count()
	context_dict_all['unread_counter'] = mailbox.objects.filter(classifications='Unread').count()
	context_dict_all['read_counter'] = mailbox.objects.filter(classifications='Read').count()
	return render(request, 'messages.html', context_dict_all)

@login_required(login_url="login")
def unread(request):

	context_dict_all = {}

	context_dict_all['inbox'] = mailbox.objects.filter(classifications='Unread')
	context_dict_all['all_messages'] = mailbox.objects.all().count()
	context_dict_all['unread_counter'] = mailbox.objects.filter(classifications='Unread').count()
	context_dict_all['read_counter'] = mailbox.objects.filter(classifications='Read').count()
	return render(request, 'unread.html', context_dict_all)

@login_required(login_url="login")
def read(request):
	context_dict_all = {}

	context_dict_all['inbox'] = mailbox.objects.filter(classifications='Read')
	context_dict_all['all_messages'] = mailbox.objects.all().count()
	context_dict_all['unread_counter'] = mailbox.objects.filter(classifications='Unread').count()
	context_dict_all['read_counter'] = mailbox.objects.filter(classifications='Read').count()
	return render(request, 'read.html', context_dict_all)



def login(request):
	secure = {}

	secure.update(csrf(request))
	return render(request, 'login.html', secure)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('messages')
	else:
		return HttpResponseRedirect('invalid')

def invalid_login(request):
	return render(request, 'invalid.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('login')

@login_required(login_url="login")
def message_view(request, message_id):
	
	context_dict_all = {}
	context_dict_all['mailbox'] = mailbox.objects.all()
	context_dict_all['sender'] = mailbox.objects.get(pk=message_id)
	mailbox.objects.filter(id = message_id).update(classifications='Read')
	context_dict_all['unread_counter'] = mailbox.objects.filter(classifications='Unread').count()
	context_dict_all['read_counter'] = mailbox.objects.filter(classifications='Read').count()
	context_dict_all['all_messages'] = mailbox.objects.all().count()
	return render(request, 'message_view.html', context_dict_all)

