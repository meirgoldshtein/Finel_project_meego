class Customer:
    def __init__(self, fname, lname, id ,phone ,debt ,date) -> None:
        self._fname = fname
        self._lname = lname
        self._id = int(id)
        self._phone = phone
        self._debt = int(debt)
        self._date = date

    @property
    def fname(self) -> str:
        return self._fname

    @property
    def lname(self) -> str:
        return self._lname
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def phone(self) -> str:
        return self._phone
    
    @property
    def debt(self) -> int:
        return self._debt

    @property
    def data(self) -> str:
        return self._date
    
    
    def add_debt(self, debt):
        if type(debt) is not int:
            print("Error: debt is not an int ! ")
            return
        self._debt += debt

    
    def __str__(self):
        return (f"name: {self._fname} {self._lname} \nid:{ self._id}\ndebt: {self._debt}\n-----------")





