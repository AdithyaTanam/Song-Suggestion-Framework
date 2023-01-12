import csv
mylist = []
with open('songlist.csv', mode='r', encoding='utf-8') as infile:
	reader = csv.reader(infile)
	for rows in reader:
		list.append(rows)
	for i in list:
		print(list)