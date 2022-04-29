from django.urls import path, include
from rest_framework import routers

from .views import (ApplicationApi, SponsorApi, StudentAPIView,
                    SponsorUpdateApi,  StudentUpdateApi,
                    StudentCreateApi, Student_sponsorListView,
                    dashboard, Student_sponsorCreateView, Student_sponsorUpdateView)


urlpatterns = [
    path('', include('dj_rest_auth.urls')),

    #sponsor
    path('application/', ApplicationApi.as_view()),
    path('sponsor/', SponsorApi.as_view()),
    path('sponsor/<int:pk>/', SponsorUpdateApi.as_view(), name='retrieve-sponsor'),

    #student
    path('student/', StudentAPIView.as_view()),
    path('student/create/', StudentCreateApi.as_view()),
    path('student/<int:pk>/', StudentUpdateApi.as_view()),

    #sponsor-student
    path('sponsor-student/', Student_sponsorListView.as_view()),
    path('sponsor-student/create/', Student_sponsorCreateView.as_view()),
    path('sponsor-student/<int:pk>/', Student_sponsorUpdateView.as_view()),

    #dashboard
    path('dashboard/', dashboard, name='dashboard')
]






