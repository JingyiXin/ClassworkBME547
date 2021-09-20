oed = {"day": "when the sun is up",
       "night": "when the moon is out"}
oed["lunch"] = "what I eat after class"

print(oed["night"])

time = "night"
print(oed[time])

oed["prime numbers"] = [1,2,3,5,7,11,13,17]
for num in oed["prime numbers"]:
    print(num)
    
if oed.get("dinner") == None:
    print("no key")
    
for i in oed:
    print("the key is {}. The value is {}.".format(i, oed[i]))
    
