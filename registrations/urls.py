from django.urls import path, include
from django.conf.urls import url

from . import views
from .views import RegistrationListView, JoinEventView, RegistrationDetailView

urlpatterns = [
    path("events/<int:event_pk>/participants/", RegistrationListView.as_view(), name="registration_list"),
    path("events/<int:event_pk>/join/", JoinEventView.as_view(), name="event_join"),
    path("registration/<int:pk>/", RegistrationDetailView.as_view(), name="registration_detail")
    # path('registration/<int:pk>/$', views.approve, name='approve'),
    # path('registration/<int:pk>/$', views.disapprove, name='disapprove'),
    # path("approve", views.approve(participant), name='approve'),
    # # # path("disapprove", views.disapprove(particpant), name='disapprove')
    #  url(r'^registration/(?P<pk>\d+)/$', views.approve, name='approve1'),
    #  url(r'^registration/(?P<pk>\d+)/$', views.disapprove, name='disapprove')
    
]