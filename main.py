import requests
import os
import datetime

API_URL = "https://pixe.la/v1/users"
Key = os.environ.get("ACCOUNT_SID")

parameter = {
    "token": Key,
    "username": "kamolesh",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# user creation
# response = requests.post(url=API_URL, json=parameter)
# response.raise_for_status()
# print(response.text)

API_GRAPH_URL = f"{API_URL}/kamolesh/graphs"
graph_parameter = {
    "id": "codingtime",
    "name": "Coding-Time-Tracker",
    "unit": "minute",
    "type": "int",
    "color": "sora"
}

header = {
    "X-USER-TOKEN": Key
}

# response = requests.post(url=API_GRAPH_URL, json=graph_parameter, headers=header)
# print(response)

# graph creation and put pixel
API_POST_URL = f"{API_GRAPH_URL}/codingtime"

# today = datetime.datetime(year=2022, day=6, month=7)
today = datetime.datetime.now()

post_parameter = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "210"
}

# response = requests.post(url=API_POST_URL, json=post_parameter, headers=header)
# print(response)

# update a pixel
UPDATE_PIXEL_URL = f"{API_POST_URL}/{today.strftime('%Y%m%d')}"

update_parameter = {
    "quantity": "200"
}

# response = requests.put(url=UPDATE_PIXEL_URL, json=update_parameter, headers=header)
# print(response)

# delete a pixel
# response = requests.delete(url=UPDATE_PIXEL_URL, headers=header)
