import requests


server_name = "https://api.github.com/"
r = requests.get(server_name + "repos/dward2/BME547/branches")

print(r)
print(type(r))
print(r.status_code)
# print(r.text)

# put into list of dictionaries, in json format
# type in https://api.github.com/repos/dward2/BME547/branches into browser to get same info
branches = r.json()
print(branches)
for branch in branches:
    print(branch["name"])
