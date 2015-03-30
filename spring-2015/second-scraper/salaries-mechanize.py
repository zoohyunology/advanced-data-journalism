import csv
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

########## STEP 1: Open and read the URL ##########

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/searchemployees.aspx'

# Create a new browser object and open the URL
br = Browser()
br.open(url)

########## STEP 2: Select and fill out the appropriate form ##########

# Select the appropriate form, which we'll find by looking in Chrome
br.select_form("ctl01")

# Each control can be set. Dropdown lists are handled as lists, text fields take text
br.form['SearchEmployees1$CalendarYear1$ddlCalendarYear'] = ['2013']
br.form['SearchEmployees1$ddlAgencies'] = ['931']
br.form['SearchEmployees1$txtLastName'] = '%'

# Submit the form
br.submit()

########## STEP 3: Grab and parse the HTML ##########

soup = BeautifulSoup(br.response())
employees = soup.find('table', id="grdEmployees")

########## STEP 4: Iterate through the results and write to an output list ##########

output = []
for tr in employees.findAll('tr')[1:]:

    output_row = []
    for td in tr.findAll('td'):
        output_row.append(td.text)

    output.append(output_row)

########## STEP 5: Write results to file ##########

print output

with open('out-mechanize.csv', 'w') as csvfile:
    my_writer = csv.writer(csvfile, delimiter='|')
    my_writer.writerows(output)
