import json

my_info = {'name' : 'chris', 'job': 'programmer', 'language':['kor', 'eng']}

json.dumps(my_info)

with open('./my_info.json', 'w') as J : json.dump(my_info, J)

with open('./my_info.json', 'r') as K : load_info = json.load(K)

print(load_info)

"""
if you want to not ascii code

=>json.dump(data, file, ensure_ascii=False)

"""
