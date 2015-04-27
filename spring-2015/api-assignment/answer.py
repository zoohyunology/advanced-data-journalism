import urllib2, json

# Replace this with your own
API_KEY = 'd7b45f3b788240acb4ab8c8aa56d7446'

########## YOUR CODE GOES HERE ##########


def get_bills(state, subjects):
    '''
    This function should accomplish the following tasks:
      - Open a connection to the /bills/ endpoing of Sunlight Foundation's OpenStates API:
        http://sunlightlabs.github.io/openstates-api/bills.html#methods/bill-search
      - Retrieve an API response with bills from the current legislative session in Missouri
      - print the titles of bills that contain "Transportation" in the "subjects" list
    '''

    # Subtle distinction here but the argument in the url should be "subjects", not "subject"
    # otherwise nothing is returned
    response = urllib2.urlopen('http://openstates.org/api/v1/bills/?state=%s&search_window=session&subjects=%s&apikey=%s' % (state, subjects, API_KEY))
    json_object = json.load(response)
    
    for bill in json_object:
        print bill['title']

    return

########## RUN FUNCTIONS HERE ##########
# Uncomment this to run your function with the appropriate arguments, as specified above

get_bills('mo', 'transportation')
