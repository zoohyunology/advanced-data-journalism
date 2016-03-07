import csv

old = open('./data/cleanme.csv', 'r')

reader = csv.DictReader(old)

for taco in reader: 
    taco['first_name'] = taco['first_name'].upper()
    taco['zip'] = taco['zip'].zfill(5)
    taco['city'] = taco['city'].replace('&nbsp;',' ')
    if int(taco['amount']) >= 1000:
        print taco
