from django.db import models

class JobPost(models.Model):
    job_title = models.CharField(max_length=255, default='')  # Title of the job
    job_type = models.CharField(max_length=100, default='')  # Type of the job (e.g., full-time, part-time)
    close_date = models.DateField(null=True, blank=True)  # Date the job post closes
    company_name = models.CharField(max_length=255, null=True, blank=True)  # Name of the company
    job_link = models.URLField(max_length=500, null=True, blank=True)  # URL link to the job post
    position_details = models.TextField(default='')  # Job description or details from the scraped page
    release_date = models.DateField(null=True, blank=True)  # The advertised or release date of the job post
    location = models.CharField(max_length=100, default='Canberra')  # Location of the job (default set to Canberra)
    job_origin = models.CharField(max_length=255, default='ACT Government Website')  # Source of the job post

    scraped_date = models.DateTimeField(auto_now_add=True)  # Date and time the job post was scraped

    def __str__(self):
        return self.job_title
