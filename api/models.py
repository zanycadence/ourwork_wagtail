from django.db import models
from ml import * 
from feature_dicts import *
# helpers ml <-> model

def flip_dict(d):
    flipped = {};
    for k,v in d.items():
        flipped[v] = k

    return flipped

def array_to_string(arr):
    s = ""
    for x in arr:
        s += str(x) + ","
    return s[:-1]

job_to_feature = {
     "Transportation": 1
    ,"Retail": 2
    ,"Manufacture":3
    ,"Security":4
    ,"Food": 5

    }

progress_to_feature ={
    "Student":1
    ,"Mentor":2
    ,"Projects":3
}

track_to_feature = {
    "Web Development":1
    ,"Data Analytics":2
    ,"Design":3
}

skills_dict={
    "HTML":0
    ,"CSS":1
    ,"Javascript":2
    ,"MongoDB":3 
    ,"SQL":4 
    ,"Python":5
    , "R":6 
    , "Tableau":7 
    ,"MATLAB":8 
    , "SAS":9
    , "Visual Studio":10
    , "Photoshop":11 
    , "Illustrator":12
    , "PHP":13
    , "NodeJS":14 
    , "Sketch":15
    , "Angular":16
    }

feature_to_job = flip_dict(job_to_feature)

# we need to map strings to integers for making actual predictions
class Member(models.Model):
    ### background - match with the mentor on this
    job = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    ### will be set on create
    mentors = models.TextField(default='null')
    mentor = models.TextField(default='null')

    ### track/specialization, will be set on create after matched with mentor
    track = models.CharField(max_length=100)
    # Entry | Project | Mentor
    track_progress = models.CharField(max_length=100)

    ### match with a job offer, will be set on update of track_progress to Project
    ### will be logicaly ored with the track that they are on
    skills = models.TextField()

    def save(self, *args, **kwargs):
        print("save is called!")
        ## happens on first save

        model = Model()
        
        if self.mentors == 'null':
            print("no mentor, assigning recomendtations!")
            job=job_to_feature[self.job]
            mentor_ids = model.predict_mentor(list(Member.objects.all().values()),job, self.location)

            print("recommended mentors" + str(mentor_ids))
            # default : assigning the mentor with the highest rank
            if len(mentor_ids)>0:
                self.mentors = mentor_ids[0]
        super(Member, self).save(*args, **kwargs)

        
class ContractSpec(models.Model):
    ### [0, 5]
    # javascript,aws,nodejs
    skills = models.TextField()
    employer = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        model = Model()
        recommended_candidates= model.match_skills((list(Member.objects.all().values()),self.project, self.location))
    
        super(ContractSpec, self).save(*args, **kwargs)

