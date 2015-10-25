import urllib2, json

API_KEY = '1f366e0712bd4ad6b079afe3bb993434'
WINDOW = 'session'
STATES = ['mo', 'nc']

for state in STATES:
    response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=%s&state=%s&search_window=%s' % (API_KEY, state, WINDOW)).read()

    data = json.loads(response)

    for bill in data:
        print bill['title']