from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import JobPost
from . serializers import JobPostSerializer

# Create a JobPost
# Get all JobPosts
# Delete all JobPosts
class JobPostListCreate(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

    def delete(self, request, *args, **kwargs):
        JobPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Delete specific job post according to primary key
class JobPostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    lookup_field = 'pk'