
import sys
import os
from customer import Customer
import bst
import socket

if len(sys.argv) < 2 :
    csv_file = ('./db.csv')
    # print("Error: missing csv file name !")

else:
    csv_file = (sys.argv[1])
if not os.path.exists(csv_file):
    with open(csv_file, 'w'):
        pass


def set_query_test(raw_query):
    correct_query = ["first name", "second name", "id", "phone", "dept", "date"]
    disjointed_query = raw_query[3::].split(",")
    correct = True
    message = None
    query_processed = []
    
    i = 0
    for _ in range(6):
        detail = disjointed_query[i].split("=")
        if detail[0].strip() != correct_query[i]:
            message = (f"Missing or wrong key {correct_query[i]}")
            correct = False
            return correct, message, query_processed
        else:
            query_processed.append(detail[1])
            
            i += 1
    return correct, message, query_processed


def customer_checking(customer_data: list):

    massage = ""
    correct = False
    date = customer_data[5]
    date_split = date.split("/")
    if len(customer_data) < 6:
        massage += ("One or more of the data is missing\n")
    elif len(customer_data) > 6:
        massage +=("Error, too many details have been entered\n")
    elif not customer_data[0].isalpha() or not customer_data[1].isalpha():
        massage +=("The consumer name must be of type string\n")
    elif not customer_data[2].isdigit():
        massage +=("ID must be numbers only\n")
    elif len(customer_data[2]) != 9:
        massage +=("ID is not valid. Must contain 9 digits\n")
    elif not customer_data[3].isdigit():
        massage +=("Phone number must be numbers only\n")
    elif len(customer_data[3]) != 10:
        massage +=("Phon number is not valid. Must contain 10 digits\n")
    elif not (customer_data[4].lstrip("-")).isdigit():
        massage +=("Debt is not valid. Must contain only digits\n")
    
    elif len(date_split) != 3:
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
        float(customer_data[4])
    except ValueError:
        massage +=("Debt must be numbers only\n")
        correct = False
    return correct, massage

def add_customer(customer_data):
        
    customer_data[-1] += "\n"
    customer_data = ",".join(customer_data)
    print(customer_data)
    with open(csv_file, 'a') as d: 
        d.writelines(customer_data)        
    
    customer_data = customer_data.split(",")
    id = customer_data[2]
    new_debt = int(customer_data[4])
    existing_customer = customers.get(id)
    if not existing_customer:
               
        print(customer_data)
        new_customer = Customer(*customer_data)
        customers[id] = new_customer       
        fname_bst.add_node(new_customer)
        lname_bst.add_node(new_customer)
        debt_bst.add_node(new_customer)
        ID_tree.add_node(new_customer)
        date_tree.add_node(new_customer)
        return "The consumer has been successfully added"
    else:
        old_debt = existing_customer.debt
        print(old_debt)
        id = int(id)
        debt_bst.update_dept(id, old_debt, new_debt, ID_tree)
        return "The consumer has been successfully update"




customers = {}
with open(csv_file, 'r') as d: 
    line_counter = 1
    for line in d.readlines():

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
            print(f"Error in line {line_counter} ->->->{correcting[1]}")
        line_counter += 1


fname_bst = bst.Fname_tree()
lname_bst = bst.Lname_tree()
debt_bst = bst.Debt_tree()
ID_tree = bst.Id_tree()
date_tree = bst.Date_tree()

for customer in customers.values():
    fname_bst.add_node(customer)
    lname_bst.add_node(customer)
    debt_bst.add_node(customer)
    ID_tree.add_node(customer)
    date_tree.add_node(customer)


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

def q_select(query):  
    
    filtered_list = []
    query = query.split(" ")
    # try:
    if query[1] == "first" and query[2] == "name":
        if query[3] == "=":
            filtered_list = fname_bst.search(query[4])
        elif query[3] == ">":
            filtered_list = fname_bst.search_high(query[4])
        elif query[3] == "<":
            filtered_list = fname_bst.search_low(query[4])
        elif query[3] == "!=":
            filtered_list = fname_bst.search_different(query[4])


    elif query[1] == "last" and query[2] == "name":
        if query[3] == "=":
            filtered_list = lname_bst.search(query[4])
        elif query[3] == ">":
            filtered_list = lname_bst.search_high(query[4])
        elif query[3] == "<":
            filtered_list = lname_bst.search_low(query[4])
        elif query[3] == "!=":
            filtered_list = lname_bst.search_different(query[4])            
    
    elif query[1] == "debt" and query[2] == ">":            
        filtered_list = debt_bst.search_range(int(query[3]), None)           
    elif query[1] == "debt" and query[2] == "<":
        print(query[3])
        filtered_list = debt_bst.search_range(None, int(query[3])) 
        print(filtered_list)   
    elif query[1] == "debt" and query[2] == "=":
        filtered_list = debt_bst.search_equal(int(query[3]))     
    elif query[1] == "debt" and query[2] == "!=":
        filtered_list = debt_bst.search_different(int(query[3])) 

    elif query[1] == "id":
        if query[2] == "=":
            filtered_list = ID_tree.search(int(query[3]))
        elif query[2] == ">":
            filtered_list = ID_tree.search_high(int(query[3]))
        elif query[2] == "<":
            filtered_list = ID_tree.search_low(int(query[3]))
        elif query[2] == "!=":
            filtered_list = ID_tree.search_different(int(query[3]))

    elif query[1] == "date":
        if query[2] == "=":
            filtered_list = date_tree.search(query[3])
        elif query[2] == ">":
            filtered_list = date_tree.search_high(query[3])
        elif query[2] == "<":
            filtered_list = date_tree.search_low(query[3])
        elif query[2] == "!=":
            filtered_list = date_tree.search_different(query[3])       


    # except:
    #     return "The query is invalid"
    if filtered_list:
        if  type(filtered_list) is list and len(filtered_list) > 1:    
            filtered_list.sort(key=lambda customer: customer.debt)    
        return filtered_list
    else:
        return "no result"



def q_set(query):
    
    testing_query = set_query_test(query)
    if testing_query[0]:
        testing_data =  customer_checking(testing_query[2])
        if testing_data[0]: 
            # if int(testing_query[2][4]):
                add_customer(testing_query[2])
                return "The addition was successful"
        else:
            return testing_data[1]
    else:
        return testing_query[1]



host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))
server_socket.listen(3)
print(f"Server listening on {host}:{port}")


def processing(query):

        # try:
            if query.startswith("select"):
                to_send = q_select(query)
            elif query.startswith("set"):
                to_send = q_set(query)        
            elif query == "quit":
                quit()
            return to_send
        #     else:
        #         raise ValueError("Invalid query")
        # except ValueError:
        #         print("Invalid query please enter again")
         



client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")
while True:
    
    
    query = client_socket.recv(4096).decode('utf-8')   
    to_send = processing(query)
    end = "$finish$".encode('utf-8')
    if type(to_send) is list:
        print(to_send)
        n = 1
        for customer in to_send:
            to_send = (f"name: {customer.fname} {customer.lname}, ID: {customer.id}, phone: {customer.phone}, debt: {customer.debt}, date: {customer.date[:-1]}")
            print(n, to_send)
            n += 1
            to_send = to_send.encode('utf-8')
            client_socket.send(to_send)
        
    
    else:
        to_send = to_send.encode('utf-8')
        client_socket.send(to_send)
    client_socket.send(end)
    print("An answer to the query has been sent")







        

# set first name=Meir, second name=Berdichevsky, id=123422789, phone=0544123456, dept=-300, date=3/4/2022

