import urllib2

response = urllib2.urlopen('http://realtime.influenceexplorer.com/api/new_filing/?page=2&page_size=10&format=json&apikey=d7b45f3b788240acb4ab8c8aa56d7446')

print response.read()
