import csv

csvfile = open('./data/cleanme.csv', 'r')
outfile = open('./data/clean.csv', 'w')

readbot = csv.DictReader(csvfile)
writebot = csv.DictWriter(outfile, readbot.fieldnames)

writebot.writeheader()

for row in readbot:
    row['first_name'] = row['first_name'].upper()
    row['city'] = row['city'].replace('&nbsp;', ' ')
    row['zip'] = row['zip'].zfill(5)

    if int(row['amount']) >= 1000:
        writebot.writerow(row)
