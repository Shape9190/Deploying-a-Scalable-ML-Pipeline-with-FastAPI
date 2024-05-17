import json

import requests

url =  "http://127.0.0.1:8000"
r = requests.get(url)

# print the status code
print(r.status_code)
# print the welcome message
print(r.text)



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# send a POST using the data above
call_url = url+"/data/"
post_request = requests.post(call_url, json=data)


# print the status code
print(post_request.status_code)
# print the result
print(post_request.text)
