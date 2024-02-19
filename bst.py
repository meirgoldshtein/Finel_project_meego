# A node object for a binary tree that contains a pointer to a consumer object, and its two children
class Node:
    def __init__(self, customer) -> None:
        self.customer = customer
        self.right = None
        self.left = None
  
        
#  Binary tree sorted by first name
class Fname_tree:
    
    def __init__(self) -> None:        
        self.root = None
        
    def add_node(self, customer):

        node = Node(customer)

        if self.root is None:
            self.root = node
            return
        
        temp = self.root
        while True:

            if node.customer.fname > temp.customer.fname:                
                if not temp.right:
                    temp.right = node
                    return
                temp = temp.right
            
            else:                
                if not temp.left:
                    temp.left = node
                    return
                temp = temp.left

    def search(self, fname):
        if not self.root:
            return
        
        target_list = []
        temp = self.root
        while temp:
            if temp.customer.fname == fname:
                target_list.append(temp.customer)
                temp = temp.left
            elif temp.customer.fname < fname:
                temp = temp.right
            elif temp.customer.fname > fname:
                temp = temp.left
        return target_list
       

class Lname_tree:
    
    def __init__(self) -> None:        
        self.root = None
        
    def add_node(self, customer):
        
        node = Node(customer)
        if self.root is None:
            self.root = node
            return
        
        temp = self.root
        while True:
            if node.customer.lname > temp.customer.lname:
                
                if not temp.right:
                    temp.right = node
                    return
                temp = temp.right
            
            else:                
                if not temp.left:
                    temp.left = node
                    return
                temp = temp.left

    def search(self, lname):
        if not self.root:
            return
        
        target_list = []
        temp = self.root
        while temp:
            if temp.customer.lname == lname:
                target_list.append(temp.customer)
                temp = temp.left
            elif temp.customer.lname < lname:
                temp = temp.right
            elif temp.customer.lname > lname:
                temp = temp.left
        return target_list


class Debt_tree:
    
    def __init__(self) -> None:        
        self.root = None


    def add_node(self, customer):
        
        node = Node(customer)
        if self.root is None:
            self.root = node
            return
        
        temp = self.root
        while True:
            
            
            if node.customer.debt > temp.customer.debt:
                
                if not temp.right:
                    temp.right = node
                    return
                temp = temp.right
            
            else:                
                if not temp.left:
                    temp.left = node
                    return
                temp = temp.left

    def search(self, low_debt, high_debt, temp="start"):
        if temp is None or not self.root:
            return []

        if temp == "start":
            temp = self.root

        if low_debt and high_debt:
            print("1")
            if low_debt <= temp.customer.debt <= high_debt:
                return [temp.customer] + self.search(low_debt, high_debt, temp.right) + self.search(low_debt, high_debt, temp.left)

            elif low_debt > temp.customer.debt:
                return self.search(low_debt, high_debt, temp.right)
            elif high_debt < temp.customer.debt:
                return self.search(self, low_debt, high_debt, temp.left)
        
        elif low_debt and not high_debt:
            print("2") 
            if low_debt <= temp.customer.debt:
                return [temp.customer] + self.search(low_debt, high_debt, temp.right) + self.search(low_debt, high_debt, temp.left)

            elif low_debt > temp.customer.debt:
                return self.search(low_debt, high_debt, temp.right)

        elif not low_debt and high_debt: 
            print("3")           
            if temp.customer.debt < high_debt:
                return [temp.customer] + self.search(low_debt, high_debt, temp.right) + self.search(low_debt, high_debt, temp.left)

            elif high_debt == temp.customer.debt:
                return [temp.customer] + self.search(low_debt, high_debt, temp.left)  

            elif temp.customer.debt > high_debt:  
                return self.search(low_debt, high_debt, temp.left)

#  Binary tree sorted by ID
class Id_tree:
    
    def __init__(self) -> None:        
        self.root = None
        
    def add_node(self, customer):
        
        node = Node(customer)
        if self.root is None:
            self.root = node
            return
        
        temp = self.root
        while True:
    
            if node.customer.id > temp.customer.id:
                if temp.right is None:
                    temp.right = node   
                    return
                temp = temp.right
           
            else:                              
                if temp.left is None:
                    temp.left = node
                    return
                temp = temp.left


    def search(self, id):
        if not self.root:
            return
        temp = self.root
        while temp:
            if temp.customer.id == id:
                return temp.customer
            if temp.customer.id < id:
                temp = temp.right
            elif temp.customer.id > id:
                temp = temp.left
        return -1









        
