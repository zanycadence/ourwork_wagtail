import csv,os
from api.models import *


currDir = os.path.dirname(os.path.realpath('__file__'))
#csvFile = os.path.join(currDir,"../dataset/member.csv")

csvFile = os.path.join(currDir,"dataset/member.csv")
with open(csvFile) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        r_mid = row['id']
        r_job = row['job']
        r_location = row['location']
        r_track = row['track']
        r_track_progress = row['progress']
        r_skills = row['skills']
        new_member = Member(m_id=r_mid,job=r_job,location=r_location,track=r_track,track_progress=r_track_progress,skills=r_skills)
        new_member.save()

# m=Member.objects.all().values()
