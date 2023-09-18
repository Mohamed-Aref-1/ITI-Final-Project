import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Month':2, 'Day':9, 'Departure_time':6, 'Arrival_time':6, 'Flight':5, 'Distance': 5 ,'Actual_departure_time': 5, 'Flight_duration': 5, 'Flight_departure_delay':5})

print(r.json())