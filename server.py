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




def customer_checking(customer_tata: list):

    massage = ""
    correct = False
    date = customer_tata[5]
    date_split = date.split("/")
    if len(customer_tata) < 6:
        massage += ("One or more of the data is missing\n")
    elif len(customer_tata) > 6:
        massage +=("Error, too many details have been entered\n")
    elif not customer_tata[0].isalpha() or not customer_tata[1].isalpha():
        massage +=("The consumer name must be of type string\n")
    elif not customer_tata[2].isdigit():
        massage +=("ID must be numbers only\n")
    elif len(customer_tata[2]) != 9:
        massage +=("ID is not valid. Must contain 9 digits\n")
    elif not customer_tata[3].isdigit():
        massage +=("Phone number must be numbers only\n")
    elif len(customer_tata[3]) != 10:
        massage +=("Phon number is not valid. Must contain 10 digits\n")
    
    elif not (date[1] == "/" or date[2] == "/") or not (date[4] == "/" or date[5] == "/"):
        massage +=("The date structure is incorrect Must be in the format  dd/mm/yyyy\n")

    elif not date_split[0].isdigit() or not 0 <= int(date_split[0]) <= 31:
        massage +=("The day entered is not valid\n")
    elif not date_split[1].isdigit() or not 0 <= int(date_split[1]) <= 12:
        massage +=("The month entered is not valid\n")  
    elif not date_split[2].rstrip("\n").isdigit() or not 0 <= int(date_split[2]):
        massage +=("The year entered is not valid\n")      
    
    else:
        correct = True
    try:
        float(customer_tata[4])
    except ValueError:
        massage +=("Debt must be numbers only\n")
        correct = False
    return correct, massage


customers = {}
with open(csv_file, 'r') as fd: 
    counter = 1
    for line in fd.readlines():

        fields = line.split(",")
        correcting =  customer_checking(fields)
        if correcting[0]:
            id = fields[2]
            if not customers.get(id):
                new_customer = Customer(*fields)
                customers[id] = new_customer
            else:        
                customers[id].add_debt(int(fields[4]))
        else:
            print(f"Error in line {counter} ->->->{correcting[1]}")
        counter += 1

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


def is_israeli_id(id):
    list1 = str(id).split()
    list2 = [1,2,1,2,1,2,1,2,1]
    sum = 0
    i = 0
    for i in range(len(list1)):
        x = list1[i] * list2[i]
        if x > 9:
            y = str(x)
            x = int(y)[0] + int(y)[1]
            sum += x
    if sum % 10 == 0:
        return True
    return False






while True:
    try:
        query = input(">>> ").split(" ")

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
            else:
                raise ValueError("Invalid query")         
            
            if filtered_list:
                filtered_list.sort(key=lambda customer: customer.debt)    
                print_query(filtered_list)
            else:
                print("No results")

    except ValueError:
        print("Invalid query please enter again")

        

