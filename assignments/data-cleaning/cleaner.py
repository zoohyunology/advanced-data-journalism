import csv

old = open('./data/cleanme.csv', 'r')
new = open('./data/cleanedversion.csv', 'w')

reader = csv.DictReader(old)
writer = csv.DictWriter(new, reader.fieldnames)

writer.writeheader()

for taco in reader: 
    taco['first_name'] = taco['first_name'].upper()
    taco['zip'] = taco['zip'].zfill(5)
    taco['city'] = taco['city'].replace('&nbsp;',' ')
    if int(taco['amount']) >= 1000:
        writer.writerow(taco)
