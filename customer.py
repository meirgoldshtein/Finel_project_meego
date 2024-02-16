class Customer:
    def __init__(self, first, last, id ,phon ,debt ,date) -> None:
        self._first = first
        self._last = last
        self._id = int(id)
        self._phon = phon
        self._debt = int(debt)
        self._date = date

    @property
    def id(self) -> int:
        return self._id

    @property
    def debt(self) -> int:
        return self._debt
    
    
    def add_debt(self, debt):
        if type(debt) is not int:
            print("Error: debt is not an int ! ")
            return
        self._debt += debt

    
    def __str__(self):
        return (f"name: {self._first} {self._last} \nid:{ self._id}\ndebt: {self._debt}\n-----------")





