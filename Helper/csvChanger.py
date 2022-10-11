# Changing CSV Delimiter
import csv

reader = csv.reader(open("coords.csv", "rU"), delimiter=';')
writer = csv.writer(open("output1.csv", 'w', newline=''), delimiter=',')
writer.writerows(reader)

print("Delimiter successfully changed")