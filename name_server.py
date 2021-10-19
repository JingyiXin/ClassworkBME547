import requests


server_name = "http://vcm-21170.vm.duke.edu:5000/"

r = requests.get(server_name)

me = {
   "name": "Jenny Xin",
   "net_id": "jx75",
   "e-mail": "jingyi.xin@duke.edu"
   }

request_json = (me)

r = requests.post(server_name + "student", json=request_json)

if (r.status_code != 200):
    print(r.text)
    
print(r.json())


