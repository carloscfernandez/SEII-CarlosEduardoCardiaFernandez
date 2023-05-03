
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

#    for line in csv_reader:
 #       print(line['e-mail'])

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames, delimiter='\t')
        csv_writer.writerheader()

        
  #  next(csv_reader)

    for line in csv_reader:
        del line['email']
        csv_writer.writerow(line)
