import json

with open('obama.json', 'r') as f:
    #json_string = f.read()
    #print json_string

    json_object = json.load(f)

    print 'Raw results object'
    print json_object

    print 'Candidate name:'
    print json_object['results'][0]['candidate_name']
    
    print 'Candidate receipts:'
    print json_object['results'][0]['total_receipts']
