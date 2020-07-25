import requests
url = 'http://localhost:5000/'
r = requests.post(url, json={'Avg. Area Income' : 79545.45857431678, 
                'Avg. Area House Age' : 5.682861321615587, 
                'Avg. Area Number of Rooms' : 7.009188142792237, 
                'Avg. Area Number of Bedrooms' : 4.09,
                'Area Population' : 23086.800502686456})           
print(r.json())
