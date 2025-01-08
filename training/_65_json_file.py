import json

my_dict = {"Name": "Narendra Modi", "Skill":["Fire in eyes", "56 inch", "Sigma male"], "Daily routine": "Bashing Pakistan"}
my_dict_2 = {"Name": "Virat Kohli", "Skill":["Aggression", "Ben Stokes", "Being GOAT"], "Strength": "Bashing Pakistan"}
my_data = [my_dict, my_dict_2]

req_file = "demo_3_.json"

fo = open(req_file, "w")
json.dump(my_data, fo, indent = 4)
fo.close()

fo = open(req_file, "r")
print(json.load(fo))
fo.close()
