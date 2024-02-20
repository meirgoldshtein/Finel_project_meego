import csv
import sys
import os
import socket
from customer import Customer
import bst

if len(sys.argv) < 2 :
    csv_file = ('./db.csv')
    print("Error: missing csv file name !")


# csv_file = (sys.argv[1])
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
    print(customer.fname + customer.lname)

fname_bst = bst.Fname_tree()
lname_bst = bst.Lname_tree()
debt_bst = bst.Debt_tree()
ID_tree = bst.Id_tree()

for customer in customers_list:
    fname_bst.add_node(customer)
    lname_bst.add_node(customer)
    debt_bst.add_node(customer)
    ID_tree.add_node(customer)

def print_query(filtered_list):
    for customer in filtered_list:
        print (f"name: {customer.fname} {customer.lname}, ID: {customer.id}, phone: {customer.phone}, debt: {customer.debt}, date: {customer.data}\n")
     
while True:
    query = input(">>> ").split(" ")
    print(query)
    if query == "quit":
        quit()
    elif query[0] == "select":
        if query[1] == "first" and query[2] == "name" and query[3] == "=":
            filtered_list = fname_bst.search(query[4])
        elif query[1] == "last" and query[2] == "name" and query[3] == "=":
            filtered_list = lname_bst.search(query[4])
        elif query[1] == "debt" and query[2] == ">":            
            filtered_list = debt_bst.search_range(int(query[3]), None)           
        elif query[1] == "debt" and query[2] == "<":
            filtered_list = debt_bst.search_range(None, int(query[3]))    
        elif query[1] == "debt" and query[2] == "=":
            filtered_list = debt_bst.search_equal(int(query[3]))     
        elif query[1] == "debt" and query[2] == "!=":
            filtered_list = debt_bst.search_different(int(query[3]))          
        print_query(filtered_list)

        


