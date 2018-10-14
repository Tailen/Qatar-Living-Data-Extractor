import csv

with open('./output.csv', 'r', newline='') as fin, open('./formatted_output.csv', 'w', newline='') as fout:
    csv_reader = csv.reader(fin, delimiter=',')
    csv_writer = csv.writer(fout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in csv_reader:
        processed_row = row[0].split(', ')
        processed_row.append(row[1])
        csv_writer.writerow(processed_row)
