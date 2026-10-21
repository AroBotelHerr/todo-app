import csv


with open('weather.csv', "r") as file:
    data = list(csv.reader(file))

city = input("Enter City: ")

for row in data[1:]:
    # In this case data info starts from
    #Austin column (C1)
    if row[0] == city:
        #gets the value of row 1 value
        print(row[0])

