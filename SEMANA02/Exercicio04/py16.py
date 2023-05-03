
import csv

html_output = ''
names = []

with open('parons.csv', 'r') as data_file:
    csv_data=csv.DictReader(data_file)

  #  for item in csv_data:
  #      print (item)

#Tirar o título e daixar os dados
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line['FirtName'] == 'No Reward':
            break
        names,append(f "{line['FirtName']} {line['LastName']}")

html_output += f '<p>There are curently {len(names)} public contributors. Thank you:</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\nt<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

#for name in names:
 #   print(name)
