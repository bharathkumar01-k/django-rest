from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_response),
    path("echo_data/",views.echo_data)
]
