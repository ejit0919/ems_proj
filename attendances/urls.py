from django.urls import path

from .views import Temp

urlpatterns = [
    path("attendances/", Temp.as_view(), name="temp"),
]