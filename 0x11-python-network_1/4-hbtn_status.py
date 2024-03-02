#!/usr/bin/python3
import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)
data = response.json()

print("Body response:")
print("\t- type: {}".format(type(data)))
print("\t- content: {}".format(data['status']))
