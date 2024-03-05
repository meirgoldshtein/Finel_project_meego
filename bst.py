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

    def search_high(self, fname):
        
        result = []
        def traverse(node):
            if node:
                if node.customer.fname > fname:
                    result.append(node.customer)
                traverse(node.left)
                traverse(node.right)                              
        traverse(self.root)
        return result
    
    
    def search_low(self, fname, temp="start"):
        
        if not self.root or not temp:
            return[]
               
        if temp == "start":
            temp = self.root
        if temp.customer.fname <= fname:
            return[temp.customer] + self.search_low(fname, temp.right) + self.search_low(fname, temp.left)
        elif temp.customer.fname > fname:           
            return self.search_low(fname, temp.left)

    
    def search_different(self, fname, temp="start"):
        
        if not self.root or not temp:
            return[]
               
        if temp == "start":
            temp = self.root
        if temp.customer.fname != fname:
            return [temp.customer] + self.search_different(fname, temp.right) + self.search_different(fname, temp.left) 
        else:
            return self.search_high(fname, temp.right) + self.search_different(fname, temp.left)     

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

    def search_high(self, lname, temp="start"):
        
        if not self.root or not temp:
            return[]
               
        if temp == "start":
            temp = self.root
        if temp.customer.lname <= lname:
            return self.search_high(lname, temp.right)
        elif temp.customer.lname > lname:
            return [temp.customer] + self.search_high(lname, temp.right)+self.search_high(lname, temp.left)

    def search_low(self, lname, temp="start"):
        
        if not self.root or not temp:
            return[]
               
        if temp == "start":
            temp = self.root
        if temp.customer.lname <= lname:
            return[temp.customer]+ self.search_low(lname, temp.right)+self.search_low(lname, temp.left)
        elif temp.customer.lname > lname:           
            return self.search_low(lname, temp.left)

    
    def search_different(self, lname, temp="start"):
        
        if not self.root or not temp:
            return[]              
        if temp == "start":
            temp = self.root
        if temp.customer.lname != lname:
            return [temp.customer] + self.search_different(lname, temp.right) + self.search_different(lname, temp.left) 
        else:
            return self.search_different(lname, temp.right) + self.search_different(lname, temp.left)  

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

    def search_range(self, low_debt, high_debt, temp="start"):
        if temp is None or not self.root:
            return []

        if temp == "start":
            temp = self.root

        if low_debt and high_debt:
            
            if low_debt <= temp.customer.debt <= high_debt:
                return [temp.customer] + self.search_range(low_debt, high_debt, temp.right) + self.search_range(low_debt, high_debt, temp.left)

            elif low_debt > temp.customer.debt:
                return self.search_range(low_debt, high_debt, temp.right)
            elif high_debt < temp.customer.debt:
                return self.search_range(self, low_debt, high_debt, temp.left)
        
        elif low_debt and not high_debt:
             
            if low_debt <= temp.customer.debt:
                return [temp.customer] + self.search_range(low_debt, high_debt, temp.right) + self.search_range(low_debt, high_debt, temp.left)

            elif low_debt > temp.customer.debt:
                return self.search_range(low_debt, high_debt, temp.right)

        elif not low_debt and high_debt: 
                      
            if temp.customer.debt < high_debt:
                return [temp.customer] + self.search_range(low_debt, high_debt, temp.right) + self.search_range(low_debt, high_debt, temp.left)

            elif high_debt == temp.customer.debt:
                return [temp.customer] + self.search_range(low_debt, high_debt, temp.left)  

            elif temp.customer.debt > high_debt:  
                return self.search_range(low_debt, high_debt, temp.left)

 

    def search_equal(self, sum, temp="start"):
        if temp is None or not self.root:
            return []

        if temp == "start":
            temp = self.root    
        if temp.customer.debt == sum:
            return [temp.customer] + self.search_equal(sum, temp.left)
        elif temp.customer.debt > sum:
            return self.search_equal(sum, temp.left)
        elif temp.customer.debt < sum:
            return self.search_equal(sum, temp.right)

        
    def search_different(self, sum, temp="start"):
        if temp is None or not self.root:
            return []

        if temp == "start":
            temp = self.root
        if temp.customer.debt != sum:
            return [temp.customer] + self.search_different(sum, temp.left) + self.search_different(sum, temp.right)
        else:
            return self.search_different(sum, temp.left) + self.search_different(sum, temp.right)


    def search_equal_id(self, sum, id, father=None, child="start"):
        
        if child == "start":
            child = self.root 
        if child.left is None or child.right is None or not self.root:
            return father, child
        if child.customer.debt == sum and child.customer.id == id:
            return father, child
        elif child.customer.debt >= sum:
            return self.search_equal_id(sum, id, child, child.left)
        elif child.customer.debt < sum:
            return self.search_equal_id(sum, id, child, child.right)


    def max_node(self, father, node):
        if not node or not node.right:
            return father, node
        return self.max_node(node, node.right)


    def update_dept(self, id, old_debt, new_debt, id_tree):
        
        target_customer = id_tree.search(id)
        if target_customer:
            prev_debt = old_debt
        else:
            print("customer not fund")
            return False
        father, child = self.search_equal_id(prev_debt, id,) 
        print(father.customer.id)

        father_max, max_node = self.max_node(None, child.left)    
            
        
        if father and child: 
            
            if not max_node:
                if father.right is child:
                    father.right = child.right
                elif father.left is child: 
                    father.left = child.right 

   
            elif max_node:
                if father_max:
                    father_max.right = None
                
                max_node.right, max_node.left = child.right, child.left
                if father.right is child:
                    father.right = max_node
                elif father.left is child:
                    father.left = max_node
        
        elif not father and child:   
            max_node.right, max_node.left = child.right, child.left
            self.root = max_node
            if father_max:
                father_max.right = None
            
        
        child.customer.debt = new_debt
        print(child.customer.debt)    
        self.add_node(child.customer)          


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
        return False


    def search_high(self, id, temp="start"):
        
        if not self.root or not temp:
            return[]
               
        if temp == "start":
            temp = self.root
        if temp.customer.id <= id:
            return self.search_high(id, temp.right)
        elif temp.customer.id > id:
            return [temp.customer] + self.search_high(id, temp.right)+self.search_high(id, temp.left)

    def search_low(self, id, temp="start"):
        
        if not self.root or not temp:
            return[]
               
        if temp == "start":
            temp = self.root
        if temp.customer.id <= id:
            return[temp.customer]+ self.search_low(id, temp.right)+self.search_low(id, temp.left)
        elif temp.customer.id > id:           
            return self.search_low(id, temp.left)

    
    def search_different(self, id, temp="start"):
        
        if not self.root or not temp:
            return[]
               
        if temp == "start":
            temp = self.root
        if temp.customer.id != id:
            return [temp.customer] + self.search_different(id, temp.right) + self.search_different(id, temp.left) 
        else:
            return self.search_different(id, temp.right) + self.search_different(id, temp.left) 


class Date_tree:

    def __init__(self) -> None:        
        self.root = None
        

    def calculate(date):
        date = date.split("/")
        return (int(date[2])*365) + (int(date[1])*31) + (int(date[0]))


    def add_node(self, customer):
        
        node = Node(customer)
        if self.root is None:
            self.root = node
            return

               
        temp = self.root
        while True:
 
            if self.calculate(node.customer.date) > self.calculate(temp.customer.date):
                if temp.right is None:
                    temp.right = node   
                    return
                temp = temp.right
           
            else:                              
                if temp.left is None:
                    temp.left = node
                    return
                temp = temp.left



    def search(self, data):
        if not self.root:
            return
        temp = self.root
        while temp:
            if self.calculate(temp.customer.data) == self.calculate(data):
                return temp.customer
            if self.calculate(temp.customer.data) < self.calculate(data):
                temp = temp.right
            elif self.calculate(temp.customer.data) > self.calculate(data):
                temp = temp.left
        return False


    def search_high(self, data, temp="start"):
        
        if not self.root:
            return[]
               
        if temp == "start":
            temp = self.root
        if temp.customer.data <= data:
            return self.search_high(data, temp.right)
        elif temp.customer.data > data:
            return [temp.customer] + self.search_high(data, temp.right)+self.search_high(data, temp.left)

    def search_low(self, data, temp="start"):
        
        if not self.root:
            return[]
               
        if temp == "start":
            temp = self.root
            target_list = []
        if temp.customer.data <= data:
            target_list.append(temp.customer)
            return[temp.customer]+ self.search_high(data, temp.right)+self.search_high(data, temp.left)
        elif temp.customer.data > data:           
            return self.search_high(data, temp.left)

    
    def search_different(self, data, temp="start"):
        
        if not self.root:
            return[]
               
        if temp == "start":
            temp = self.root
        if temp.customer.data != data:
            return [temp.customer] + self.search_high(data, temp.right) + self.search_high(data, temp.left) 
        else:
            return self.search_high(data, temp.right) + self.search_high(data, temp.left) 
        
