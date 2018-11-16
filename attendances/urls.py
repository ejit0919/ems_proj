from django.urls import path
from django.conf.urls import url

from .views import AttendanceSummaryView, AttendanceView

urlpatterns = [
    path("events/<int:event_pk>/attendance", AttendanceSummaryView.as_view(), name="attendance"),
]