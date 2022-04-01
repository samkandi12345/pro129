import csv
dataset1 = []
dataset2 = []

with open("new_bright_star_data_2.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("new_dwarf_star_data_2.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

header1 = dataset1[0]
star_data = dataset1[1:]
header2 = dataset2[0]
star_data2 = dataset2[1:]

headers = header1+header2
planet_data = []

for index,data_row in enumerate(star_data):
    planet_data.append(star_data[index]+star_data2[index])

with open("new.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)



