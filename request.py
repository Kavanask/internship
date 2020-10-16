import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={ 'aggrigate':9, 'interview_score':6, 'Java':1,'Python':1,'C':1,'C++':1})

print(r.json())