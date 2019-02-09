from django.db import models

# we need to map strings to integers for making actual predictions
class Member(models.Model):
    ### background - match with the mentor on this
    m_id = models.CharField(max_length=10,default='null')
    job = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    ### track/specialization
    track = models.CharField(max_length=100)
    # Entry | Project | Mentor
    track_progress = models.CharField(max_length=100)

    ### match with a job offer
    skills = models.TextField()

class ContractSpec(models.Model):
    ### [0, 5]
    # javascript,aws,nodejs
    skills = models.TextField()

    employer = models.CharField(max_length=100)

    
