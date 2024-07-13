from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("home/", views.homepage, name="homepage"),
    path("contact/", views.contact, name="contact"),
    path("project/<int:id>/", views.project, name="project"),
]
