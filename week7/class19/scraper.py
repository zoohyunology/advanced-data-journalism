import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.open('http://a073-ils-web.nyc.gov/inmatelookup/ils/pages/common/find.jsf')

# Fill out the form
br.select_form('mainform')
br.form['mainform:sub_maincontent:fname'] = '%'
br.form['mainform:sub_maincontent:lname'] = '%'

# Submit the form
br.submit()

# Get HTML
html = br.response().read()

# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find the main table using both the "align" and "class" attributes
main_table = soup.find('table',
    {'id': 'mainform:sub_maincontent:allInmateListId'}
)

# Now get the data from each table row
for row in main_table.find_all('tr'):
    data = [cell.text for cell in row.find_all('td')]
    print data