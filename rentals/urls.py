from django.urls import path
from .views import all_reservations

urlpatterns = [
    path("", all_reservations)
]