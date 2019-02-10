## ML goes here -->
import pandas as pd
from api.models import * 

class Mentor_Model():
	# 2 - mentor code
	def predict(self,db,job_int, location_int=None,filters=5):
		df = pd.DataFrame(db)
		df2=df.loc[df['track_progress'] == '2']
		if location_int is not None:
			df2= df2.loc[df['location'] == str(location_int)]
		rank = []
		for index,row in df2.iterrows():
			score=0 
			for x in job_int :
					if x in list(row['job']) :
						score = score+1
			rank.append(score)
		df2['score'] = rank
		df2=df2.sort_values('score',ascending=False)
		print(df2[0:filters])
		return df2[0:filters]['id']

