from django.urls import path
from website.views import *

urlpatterns = [
	path('', landing_page)
]
