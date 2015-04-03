import json

with open('obama.json', 'r') as f:
    json_object = json.load(f)

    print json_object['results'][0]['candidate_name']