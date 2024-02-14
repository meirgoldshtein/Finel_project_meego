import csv
import sys
import os
import socket
from customer import Customer

if len(sys.argv) < 2 :
    print("Error: missing csv file name !")


csv_file = (sys.argv[1])
if not os.path.exists(csv_file):
    with open(csv_file, 'w'):
        pass


customers = []
with open(csv_file, 'r') as fd: 
    for line in fd.readlines():
        fields = line.split(",")
        index = -1
        id = fields[2]
        for i, customer in enumerate(customers):
            if customer.id == id:
                index = i 
                break
        if index >= 0:
            customers[index].add_debt(int(fields[4]))

        else:
            customer = Customer(*fields)
            customers.append(customer)

customers.sort(key=lambda customer: customer.debt)
for customer in customers:    
    print(customer)

        


