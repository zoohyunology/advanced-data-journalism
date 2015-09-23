import csv

# Open our input and output files
csvfile = open('./data/sample.csv', 'r')
outfile = open('./data/sample-clean.csv', 'w')

# Now a DictReader and DictWriter
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

# Write headers
writer.writeheader()

# Clean and write the data to output
for row in reader:
    row['first_name'] = row['first_name'].upper()
    writer.writerow(row)