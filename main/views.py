from django.shortcuts import render

def home(request): 
	return render(request, 'index.html') 


def properties(request):
	return render(request, 'properties.html')

def contact_view(request):
	return render(request, 'contact.html')

def proper_detail(request): 
	return render(request, 'property-details.html')