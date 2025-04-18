import csv

data = [
    ['Johnny', 87770000000],
    ['Jane', 87770000001],
    ['Bob', 87770000002]
]

with open('sample.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['first_name', 'phone_number'])

    for row in data:
        writer.writerow(row)