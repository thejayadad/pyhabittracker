
import requests
from datetime import datetime

USERNAME = "jaydunb12"
TOKEN = "sijnbadjfnbkljadnfbjdnb"
GRAPH_ID = "graph1"


pixela_api = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=pixela_api, json=user_params)

# print(response.text)

graph_api = f"{pixela_api}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Tracker",
    "unit": "minute",
    "type": "int",
    "color": "sora"
}

# graph_update = f"{graph_api}/graph1"

pix_creation = f"{pixela_api}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

graph_body_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "35"
}


response = requests.post(url=graph_api, json=graph_config, headers=headers)
update = requests.post(url=pix_creation, json=graph_body_update, headers=headers)

print(response.text)
print(update.text)
print(today)