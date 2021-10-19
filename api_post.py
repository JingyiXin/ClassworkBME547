import requests


server_name = "http://vcm-7631.vm.duke.edu:5000/"

r = requests.get(server_name + "countries")

countries = {"one": "Spain", "two": "Sweden"}
request_json = (countries)

r = requests.post(server_name + "compare", json=request_json)
if (r.status_code != 200):
    print(r.text)
print(r.json())