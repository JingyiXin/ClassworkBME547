import requests


server_name = "http://vcm-7631.vm.duke.edu:5002/"
r = requests.get(server_name + "get_patients/jx75")

print(r.text)

donor = requests.get(server_name + "get_blood_type/F1")
print(donor.text)
recipient = requests.get(server_name + "get_blood_type/M4")
print(recipient.text)

matching_json = {"Name": "jx75", "Match": "Yes"}
matching = requests.post(server_name + "match_check", json=matching_json)
print(matching.text)


