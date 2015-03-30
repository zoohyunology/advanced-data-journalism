import urllib2
import csv
from BeautifulSoup import BeautifulSoup

########## STEP 1: Open and read the URL ##########

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchResults.aspx?last=%25&first=%25&year=2013&agency=931'
html = urllib2.urlopen(url).read()

########## STEP 2: Parse HTML with BeautifulSoup ##########

soup = BeautifulSoup(html)
employees = soup.find('table', id="grdEmployees")

########## STEP 3: Iterate through the results and write to an output list ##########

output = []
for tr in employees.findAll('tr')[1:]:

    output_row = []
    for td in tr.findAll('td'):
        output_row.append(td.text)

    output.append(output_row)

########## STEP 4: Write results to file ##########

print output

with open('output-basic.csv', 'w') as csvfile:
    my_writer = csv.writer(csvfile, delimiter='|')
    my_writer.writerows(output)
