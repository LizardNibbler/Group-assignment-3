
#used to get the common things from all items
class item():
    numberofitems=0;
    def __init__(self, name, description,price,numinstock,category):
        self.set_name(name)
        self.set_description(description)
        self.set_price(price)
        self.set_numinstock(numinstock)
        self.set_category(category)
        item.numberofitems+=1
        return

    def set_name(self,name):
        self.__name=name
        return
    
    def set_description(self,description):
        self.__description=description
        return
    
    def set_price(self,price):
        self.__price=price
        return

    def set_numinstock(self,numinstock):
        self.__numinstock=numinstock
        return
    def set_category(self,category):
        self.__category=category
        return

    def get_name(self):
        return self.__name
    def get_description(self):
        return self.__description
    def get_price(self):
        return self.__price
    def get_numinstock(self):
        return self.__numinstock
    def get_categogery(self):
        return self.__category
    def display(self):
        return "Item name: "+self.__name+"\nDescription: "+self.__description+"\nPrice: "+str(self.__price)+"\nTotal in stock: "+str(self.__numinstock)+"\nCategory: "+self.__category

#super used to refer back to the partent constructor
class Book(item):
    def __init__(self,name,description,price,numinstock,category,booktype,author,genre):
        super().__init__(name,description,price,numinstock,category)
        self.set_booktype(booktype)
        self.set_author(author)
        self.set_genre(genre)
        Book.numberofbooks+=1
        return

    def set_booktype(self,booktype):
        self.__booktype=booktype
        return

    def set_author(self, author):
        self.__author=author
        return

    def set_genre(self,genre):
        self.__genre=genre
        return

    def get_booktype(self):
        return self.__booktype

    def get_author(self):
        return self.__author
        
    def get_genre(self):
        return self.__genre

    def display(self):
        display=super().display()
        return display+"\nBook Type: "+self.__booktype+"\nAuthor: "+self.__author+"\nGenre: "+self.__genre+"\n"


class household_items(item):
    def __init__(self,name,description,price,numinstock,category,department):
        super().__init__(name,description,price,numinstock,category)
        self.set_department(department)
        household_items.numberofhouseitems+=1
        return
    
    def set_department(self, department):
        self.__department=department
        return
    
    def get_department(self):
        return self.__department
    
    def display(self):
        display=super().display()
        
        return display+" "+self.__department+"\n"


class electronics(item):
    def __init__(self,name,description,price,numinstock,category,manufacturer,electronic_type):
        super().__init__(name,description,price,numinstock,category)
        self.set_manufacturer(manufacturer)
        self.set_type(electronic_type)
        electronics.numberofelectronics+=1

    def set_manufacturer(self, manu):
        self.__manu=manu
        return

    def set_type(self, eltype):
        self.__Electype=eltype
        return

    def get_manufacturer(self):
        return self.__manu
    def get_type(Self):
        return self.__Electype

    def display(self):
        display=super().display()
        return display+"\nManufacturer "+self.__manu+"\nType of Electronic: "+self.__Electype+"\n"


class toys(item):

    def __init__(self,name,description,price,numinstock,category,toytype):
        super().__init__(name,description,price,numinstock,category)
        self.set_type(toytype)
        toys.toysnum+=1
        return
    
    def set_type(self, toytype):
        self.__type=toytype
        return
    
    def get_type(self):
        return self.__type
    
    def display(self):
        display=super().display()        
        return display+"\nType of Toy: "+self.__type+"\n"



        
    




    
