
class Node:
    def __init__(self, customer) -> None:
        self.customer = customer
        self.right = None
        self.left = None
  
        



class Fname_tree:
    
    def __init__(self) -> None:        
        self.root = None
        


    def add_node(self, node):

        if self.root is None:
            self.root = node
            return
        
        temp = self.root
        while True:

            if node.customer.id == temp.customer.id:
                return

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



class Id_tree:
    
    def __init__(self) -> None:        
        self.root = None
        


    def add_node(self, node):
        if self.root is None:
            self.root = node
            return
        
        temp = self.root
        while True:
            if node.customer.id == temp.customer.id:
                return

            if node.customer.id > temp.customer.id:
                
                if temp.right is None:
                    temp.right = node
                    return
                temp = temp.right
            
            elif node.customer.id < temp.customer.id:
                
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









        
