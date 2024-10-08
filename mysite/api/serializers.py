from rest_framework import serializers
from .models import JobPost

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['id', 'job_title', 'job_type', 'close_date', 
                  'company_name', 'job_link', 'position_details', 'release_date', 
                  'location', 'job_origin', 'scraped_date']
        