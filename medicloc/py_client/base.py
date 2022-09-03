import requests



end_point = "http://127.0.0.1:8000/"

response =  requests.get(end_point, json={"country_id": 123})

print(response.json())