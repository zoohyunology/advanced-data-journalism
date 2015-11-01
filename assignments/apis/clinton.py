import re

def clean_json(json):
    '''
    Turn dirty State Department JSON into clean JSON.
    '''
    return re.sub(r'new Date\(.*?\)', '""', json)

# Apply the above function like so ...

# dirty_json = urllib2.urlopen(whatever).read()
# valid_json = clean_json(dirty_json)

# ... do things with valid_json