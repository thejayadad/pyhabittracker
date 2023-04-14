
import requests

USERNAME = "jaydunb12"
TOKEN = "sijnbadjfnbkljadnfbjdnb"


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
    "id": "graph1",
    "name": "Coding Tracker",
    "unit": "minute",
    "type": "int",
    "color": "sora"
}

response = requests.post(url=graph_api, json=graph_config, headers=headers)
print(response.text)