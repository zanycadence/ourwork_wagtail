import csv,os
from api.models import *


currDir = os.path.dirname(os.path.realpath('__file__'))
#csvFile = os.path.join(currDir,"../dataset/member.csv")

csvFile = os.path.join(currDir,"dataset/new_members.csv")

members=list(Member.objects.all().values())
print(members)

with open(csvFile) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        r_mid = row['id']
        r_job = row['industry']
        r_location = row['location']
        r_track = row['track']
        r_track_progress = row['progress']
        r_skills = row['skills']
        new_member = Member(m_id=r_mid,job=r_job,location=r_location,track=r_track,track_progress=r_track_progress,skills=r_skills)
        new_member.save()


def blah(obj):
        model = Model()
        if obj.mentor == 'null':
            #job=job_to_feature[self.job]
            mentor_ids = model.predict_mentor(list(Member.objects.all().values()),obj.job, obj.location)
            print("recommended mentors" + str(mentor_ids))
            # default : assigning the mentor with the highest rank
            #if len(mentor_ids)>0:
            obj.mentor = mentor_ids[0]


    
members=list(Member.objects.all().values())

for member in members:
    member_id = member['id']
    t = Member.objects.get(id=member_id)
    blah(t)
    t.save()

#members=list(Member.objects.all().values())


