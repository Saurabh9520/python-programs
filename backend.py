
import urllib.request
import json
import pandas as pd
import numpy as np
url = "https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences"
json_obj = urllib.request.urlopen(url)
data=json.load(json_obj)


s = pd.DataFrame(data['paid'])

#print(s)
data1=s.loc[:,'city':'country']
print(data1)
#exactly all the data is duplicate
dup=pd.DataFrame(data['paid'])
dup2=dup[dup.duplicated()]
print("exactly all the data is duplicated:  ")
print(dup2)
#duplicate confname data -----
dup1=pd.DataFrame(data['paid'],columns=['confName'])
dup3=dup1[dup1.duplicated(['confName'])]
print(dup3)
