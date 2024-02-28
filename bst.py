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

    def search_range(self, low_debt, high_debt, temp="start"):
        if temp is None or not self.root:
            return []

        if temp == "start":
            temp = self.root

        if low_debt and high_debt:
            
            if low_debt <= temp.customer.debt <= high_debt:
                return [temp.customer] + self.search(low_debt, high_debt, temp.right) + self.search(low_debt, high_debt, temp.left)

            elif low_debt > temp.customer.debt:
                return self.search(low_debt, high_debt, temp.right)
            elif high_debt < temp.customer.debt:
                return self.search(self, low_debt, high_debt, temp.left)
        
        elif low_debt and not high_debt:
             
            if low_debt <= temp.customer.debt:
                return [temp.customer] + self.search(low_debt, high_debt, temp.right) + self.search(low_debt, high_debt, temp.left)

            elif low_debt > temp.customer.debt:
                return self.search(low_debt, high_debt, temp.right)

        elif not low_debt and high_debt: 
                      
            if temp.customer.debt < high_debt:
                return [temp.customer] + self.search(low_debt, high_debt, temp.right) + self.search(low_debt, high_debt, temp.left)

            elif high_debt == temp.customer.debt:
                return [temp.customer] + self.search(low_debt, high_debt, temp.left)  

            elif temp.customer.debt > high_debt:  
                return self.search(low_debt, high_debt, temp.left)


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


    def search_equal_debt_ID(self, debt, id, temp="start"):
        if temp is None or not self.root:
            return None, None

        if temp == "start":
            temp = self.root    
            if temp.id == id and temp.debt == debt and temp is self.root:
                return None, temp
        
        if temp.left:
            if temp.left.customer.id != id:
                if temp.left.customer.debt >= debt:
                    return self.search_equal(debt, id, temp.left)
                elif temp.left.customer.debt < debt:
                    return self.search_equal(debt, id, temp.right)
            elif temp.left.customer.id == id and temp.left.customer.debt == debt:
                return temp, temp.left
        
        if temp.right:
            if temp.right.customer.id != id:
                if temp.right.customer.debt >= debt:
                    return self.search_equal(debt, id, temp.left)
                elif temp.right.customer.debt < debt:
                    return self.search_equal(debt, id, temp.right)
            elif temp.right.customer.id == id and temp.right.customer.debt == debt:
                return temp, temp.left       

    def max_node(self, father, node):
        if not node or not node.right:
            return father, node
        return self.max_node( node, node.right)


    def update_dept(self, id, new_debt):
        
        target_customer = Id_tree.search(id)
        if target_customer:
            prev_debt = target_customer.debt
        else:
            print("customer not fund")
            return False
        father, child = self.search_equal_ID(prev_debt, id,) 

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
            if father_max:
                father_max.right = None
            
        
        child.customer.debt = new_debt    
        self.add_node(Node(child.customer))          



                
        
        



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









        
