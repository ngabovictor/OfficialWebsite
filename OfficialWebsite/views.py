from django.shortcuts import render


def handler_404(request):
	response = render(request,'404.html')
	response.status_code = 404
	return response

def handler_500(request):
	response = render(request,'500.html')
	response.status_code = 500
	return response