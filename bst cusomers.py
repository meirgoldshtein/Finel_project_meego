
class Node:
    def __init__(self, first, last, id ,phon ,debt ,date) -> None:
        self._first = first
        self._last = last
        self._id = id
        self._phon = phon
        self._debt = int(debt)
        self._date = date
        self.right = None
        self.left = None
        



class Id_tree:
    
    def __init__(self) -> None:        
        self.root = None


    def add_node(self, customer):
        if self.root is None:
            self.root = customer
            return
        
        temp = self.root
        while True:
            if customer.id > temp.id:
                
                if temp.right is None:
                    temp.right = customer
                    break
                else:
                    temp = temp.right
            
            elif customer.id <= temp.id:
                
                if temp.left is None:
                    temp.left = customer
                    break
                else:
                    temp = temp.left


    def search(self, id):
        if not self.root:
            return
        temp = self.root
        while temp:
            if temp.id == id:
                return temp
            if temp.id < id:
                temp = temp.right
            elif temp.id > id:
                temp = temp.left
        return -1









        
