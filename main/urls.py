from django.contrib import admin
from django.urls import path
from .views import home, properties, contact_view, proper_detail



urlpatterns = [
	path('', home), 
	path('properties/', properties, name='properties_view'),
	path('contact/', contact_view, name="contact_view"), 
	path('detail/', proper_detail, name="detail")
]