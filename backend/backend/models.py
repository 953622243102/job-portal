from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    company=models.TextField(max_length=100)
    location=models.CharField(max_length=100)
    salary_range=models.CharField(max_length=50, blank=True)  # we give salary as an charfield like 3-5 LPA, and it is optional, so use blank=true
    posted_on=models.DateTimeField(auto_now_add=True)  #auto_now_add used to set current time
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)  #we use onDelete, because when this user deletd, then job created by user also deleted, like parent del,child also del
    
class Application(models.Model):
    STATUS_CHOICES=(
        ('pending',"Pending"),
        ('shortlisted','Shortlisted') ,      #tuple format, like key value
        ('rejected','Rejected'),
        ('hired','Hired')
    )
    job=models.ForeignKey(Job, on_delete=models.CASCADE)    #if the job is del, then application also del, so we use onDelete
    applicant=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=50, choices=STATUS_CHOICES,default='pending')    #pending/sortlisted/rejected/hired
    applied_on=models.DateTimeField(auto_now_add=True)
    
    
    
