from django.db import models

# we need to map strings to integers for making actual predictions
class Member(models.Model):
    background_job = models.CharField(max_length=100)
    background_location = models.CharField(max_length=100)
    
    track = models.CharField(max_length=100)
    # Entry | Project | Mentor
    track_progress = models.CharField(max_length=100)
    
    
