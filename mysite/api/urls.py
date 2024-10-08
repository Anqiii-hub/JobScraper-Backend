from django.urls import path
from . import views

urlpatterns = [
    path('jobposts/', views.JobPostListCreate.as_view(), name='jobpost-view-create'),
    path('jobposts/<int:pk>', views.JobPostRetriveUpdateDestroy.as_view(), name='jobpost-view-update')
]