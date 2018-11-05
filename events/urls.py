from django.urls import path

from .views import HomePageView, EventListView

urlpatterns = [
    path("", HomePageView.as_view()),
    path("events/", EventListView.as_view())
]