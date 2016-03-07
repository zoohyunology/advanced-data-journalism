import csv

# define and open our input and output files
old = open('./data/cleanme.csv', 'r')
#new = open('./data/cleanedversion.csv', 'w')

# now use DictReader and DictWriter methods within the files
reader = csv.DictReader(old)
#writer = csv.DictWriter(new, reader.fieldnames)

# write headers
#writer.writeheader()

# clean
for taco in reader: 
    taco['first_name'] = taco['first_name'].upper()
    taco['zip'] = taco['zip'].zfill(5)
    taco['city'] = taco['city'].replace('&nbsp;',' ')
    if int(taco['amount']) >= 1000:
        print taco
