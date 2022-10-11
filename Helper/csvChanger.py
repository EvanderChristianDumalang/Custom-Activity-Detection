# Changing CSV Delimiter
import csv

reader = csv.reader(
    open("directory path for csv (input)", "rU"), delimiter=';')
writer = csv.writer(open("directory path for csv (output)",
                    'w', newline=''), delimiter=',')
writer.writerows(reader)

print("Delimiter changed")
