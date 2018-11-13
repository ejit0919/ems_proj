from django.urls import path

from .views import RegistrationListView, JoinEventView

urlpatterns = [
    path("events/<int:event_pk>/participants/", RegistrationListView.as_view(), name="registration_list"),
    path("events/<int:event_pk>/join/", JoinEventView.as_view(), name="event_join")
]