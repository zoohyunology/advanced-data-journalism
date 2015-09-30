import urllib2, csv 
from BeautifulSoup import BeautifulSoup

html = urllib2.urlopen('https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s').read()