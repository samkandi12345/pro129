import csv
data = []
data2 = []

with open("bright_stars.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
header = data[0]
star_data = data[1:]
for datapoint in star_data:
    datapoint[2] = datapoint[2].lower()
star_data.sort(key=lambda star_data:star_data[2])
with open("new_bright_star_data_2.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(star_data)

with open("dwarf_stars.csv") as f:
    csvreader2 = csv.reader(f)
    for row in csvreader2:
        data2.append(row)
header = data2[0]
star_data2 = data2[1:]
for datapoint2 in star_data:
    datapoint2[2] = datapoint2[2].lower()
star_data2.sort(key=lambda star_data2:star_data2[2])
with open("new_dwarf_star_data_2.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(star_data2)