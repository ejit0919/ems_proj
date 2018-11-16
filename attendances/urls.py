from django.urls import path
from django.conf.urls import url

from .views import AttendanceSummaryView, AttendanceView, AttendanceEventDatesView

urlpatterns = [
    path("activities/my/<int:event_pk>/attendance", AttendanceSummaryView.as_view(), name="attendance_summary"),
    path("events/<int:event_pk>/attendance", AttendanceEventDatesView.as_view(), name="attendance_events"),
]