import csv
import sys
import os
import socket
from customer import Customer
import bst

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
                customer.add_debt(int(fields[4]))
                break
        else:
            new_customer = Customer(*fields)
            customers.append(new_customer)

customers.sort(key=lambda customer: customer.debt)
for customer in customers:    
    print(customer)

fname_bst = bst.Fname_tree()
ID_tree = bst.Id_tree()

for customer in customers:
    n = bst.Node(customer)
    fname_bst.add_node(n)
    # ID_tree.add_node(n)


while True:
    query = input(">>> ")
    if query == "quit":
        quit()


        


