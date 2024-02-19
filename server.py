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


customers = {}
with open(csv_file, 'r') as fd: 
    for line in fd.readlines():
        fields = line.split(",")
        id = fields[2]
        if not customers.get(id):
            new_customer = Customer(*fields)
            customers[id] = new_customer
        else:        
            customers[id].add_debt(int(fields[4]))


customers_list = list(customers.values())
customers_list.sort(key=lambda customer: customer.debt)
for customer in customers_list:    
    print(customer.id)

fname_bst = bst.Fname_tree()
lname_bst = bst.Lname_tree()
debt_bst = bst.Debt_tree()
ID_tree = bst.Id_tree()

for customer in customers_list:
    fname_bst.add_node(customer)
    lname_bst.add_node(customer)
    debt_bst.add_node(customer)
    ID_tree.add_node(customer)


# while True:
#     query = input(">>> ")
#     if query == "quit":
#         quit()


        


