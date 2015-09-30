import urllib2, csv 
from BeautifulSoup import BeautifulSoup

html = urllib2.urlopen('http://www.showmeboone.com/sheriff/jailresidents/jailresidents.asp').read()