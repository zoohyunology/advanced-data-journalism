import urllib2, json

# Replace this with your own
API_KEY = 'd7b45f3b788240acb4ab8c8aa56d7446'

def sample_function(name):
    print 'I am a sample function'
    print 'My name is %s' % name
    return

########## YOUR CODE GOES HERE ##########

def get_bills(state, type):
    '''
    This function should accomplish the following tasks:
      - Open a connection to the /bills/ endpoing of Sunlight Foundation's OpenStates API:
        http://sunlightlabs.github.io/openstates-api/bills.html#methods/bill-search
      - Retrieve an API response with bills from the current legislative session in Missouri
      - print the titles of bills that contain "Transportation" in the "subjects" list
    '''
    return

########## RUN FUNCTIONS HERE ##########

sample_function('Chase')

# Uncomment this to run your function with the appropriate arguments, as specified above
# get_bills('mo', 'Transportation')