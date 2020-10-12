#used to include the item classes
from item import *
from login import *


class Inventory():
    def __init__(self):
        
        #Gets the number for each item in stock.
        file1=open("itemsinstock.txt","r")
        x=file1.readline()
        file1.close()
        y= x.split()
        #inportant converts the array to int values
        self.__stock=[int(i) for i in y]

        #Inserts the items and pulls the stock for the array
        a= Book("Comic Book","Has pictures",30,self.__stock[0],"Book","Comic","James","action")
        b= Book("History Hook","Has History",1000,self.__stock[1],"Book","TextBook","Jay","Education")
        c= Book("Cooking Book","Has Food", 100,self.__stock[2],"Book","Cooking Book","David","Nutriution")
        self.__books= [a,b,c]
        

        d= electronics("I phone","Apple Iphone",100,self.__stock[3],"Electronics","Apple","Phone")
        e= electronics("I phone Charger","LOoks",40,self.__stock[4],"Electronics","Apply","Phone Accessoryes")
        f= electronics("TV","Used to watch Television",100,self.__stock[5],"Electronics","Viso","TV")
        self.__electronics=[d,e,f]

        g= household_items("Cleaner","cleans stuff",1,self.__stock[6],"Househould Item","Bathroom")
        h= household_items("Soap","USe it to wash yourself",10,self.__stock[7],"Househould Item","hygeine")
        j= household_items("Paper","Write on it",4,self.__stock[8],"Househould Item","Office")
        self.__householdItems=[g,h,j]
                
        k=toys("Spider Man","Marvel toy",15,self.__stock[9],"Toy","Action toy")
        l=toys("Barbie","Barabie Doll",15,self.__stock[10],"Toy","Dolls")
        m=toys("Fidget Spinner","Fidget Toy",12,self.__stock[11],"Toy","Motion Toy")
        self.__toys=[k,l,m]
        
        return

    
    #used to display all the items of a particular category
    #For example if I wanted to look at the toys it would be display_items("toys")
    def display_items(self,itemcat):
        if(itemcat=="toys"):
            itemarray=self.__toys
        elif(itemcat=="books"):
            itemarray=self.__books
        elif(itemcat=="household_items"):
            itemarray=self.__householdItems
        else:
            itemarray=self.__electronics
        
        for x in itemarray:
            print(x.display())
        print()

    #used to display a particular item in a category
    #for example if I want to look at the soap the function call would be display_item("household_items",1)
    def display_item(self,itemcat,index):
        if(itemcat=="toys"):
            itemarray=self.__toys
        elif(itemcat=="books"):
            itemarray=self.__books
        elif(itemcat=="household_items"):
            itemarray=self.__householdItems
        else:
            itemarray=self.__electronics
        print(itemarray[index].display())

        
    #used to update the invenotory after the user purchases an item
    #To call update_inventory() on the cooking book it would be the stock index and the amount(3)
    #so update_inventory(2,3)
    def update_inventory(self,index,ammount_taken):
        self.__stock[index]-=ammount_taken
        if(self.__stock[index]<0):
            self.__stock[index]=0
        file=open("itemsinstock.txt","w")
        statement=""
        for x in self.__stock:
            statement+=str(x)+" "
        file.write(statement)
        file.close()

        #updates the stock in the main program very important
        if(index<=2):
            self.__books[index].set_numinstock(self.__stock[index])
        elif(index<6):
            self.__electronics[index-3].set_numinstock(self.__stock[index])
        elif(index<9):
            self.__householdItems[index-6].set_numinstock(self.__stock[index])
        elif(index<12):
            self.__toys[index-9].set_numinstock(self.__stock[index])
    def get_price(self,index):
        if(index<=2):
            return self.__books[index].get_price()
        elif(index<6):
            return self.__electronics[index-3].get_price()
        elif(index<9):
            return self.__householdItems[index-6].get_price()
        elif(index<12):
            return self.__toys[index-9].get_price()

    def get_stock(self,index):
        if(index<=2):
            return self.__books[index].get_numinstock()
        elif(index<6):
            return self.__electronics[index-3].get_numinstock()
        elif(index<9):
            return self.__householdItems[index-6].get_numinstock()
        elif(index<12):
            return self.__toys[index-9].get_numinstock()


            
class Store():
   comic = 0
   history_book = 0
   cook_book = 0

   iphone = 0
   phone_charger = 0
   tv = 0

   cleaner = 0
   paper = 0
   soup = 0

   spider_man = 0
   barbie = 0
   fidget_spin = 0
   x= Inventory()
   def __init__(self):
       return
       #self.select_items()
       #self.total_calc()
       #self.add_items()
       #self.remove_items()
       #self.view_items()

    #Function for selecting the category and the items from the category
   def select_items(self):
        #x = Inventory()

        print("1) Book\n")
        print("2) Electronics\n")
        print("3) Household Items\n")
        print("4) Toys\n")

        c_input = input("Select a Category: ")
        c_input = int(c_input)
        print("\n")

        if (c_input == 1):
            self.x.display_items("books")
            print("\n")
            print("1) Comic Book\n")
            print("2) History Book\n")
            print("3) Cooking Book\n")

            item_select1 = input("Which item would you like to order?\n")
            item_select1 = int(item_select1)

            if(item_select1 == 1):

                comic = input("How many would you like to order?\n")
                self.comic = int(comic)
                stock=self.x.get_stock(0)
                while(stock<self.comic):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num = input("How many would you like to order?\n")
                    self.comic = int(num)
                    stock=self.x.get_stock(0)
                print("\n")

            elif(item_select1 == 2):
                history_book = input("How many would you like to order?\n")
                self.history_book = int(history_book)
                stock=self.x.get_stock(1)
                while(stock<self.history_book):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num = input("How many would you like to order?\n")
                    self.history_book = int(num)
                    stock=self.x.get_stock(1)
                print("\n")

            elif(item_select1 == 3):
                cook_book = input("How many would you like to order?\n")
                self.cook_book = int(cook_book)
                stock=self.x.get_stock(2)
                while(stock<self.cook_book):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num= input("How many would you like to order?\n")
                    self.cook_book = int(num)
                    stock=self.x.get_stock(2)
                print("\n")
                


        elif (c_input == 2):
            self.x.display_items("electronics")
            print("\n")
            print("1) Iphone\n")
            print("2) Iphone Charger\n")
            print("3) TV\n")

            item_select2 = input("Which item would you like to order?\n")
            item_select2 = int(item_select2)

            if (item_select2 == 1):

                iphone = input("How many would you like to order?\n")
                self.iphone = int(iphone)
                stock=self.x.get_stock(3)
                while(stock<self.iphone):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num = input("How many would you like to order?\n")
                    self.iphone = int(num)
                    stock=self.x.get_stock(3)
                print("\n")

            elif (item_select2 == 2):
                phone_charger = input("How many would you like to order?\n")
                self.phone_charger = int(phone_charger)
                stock=self.x.get_stock(4)
                while(stock<self.phone_charger):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num = input("How many would you like to order?\n")
                    self.phone_charger= int(num)
                    stock=self.x.get_stock(4)
                print("\n")

            elif (item_select2 == 3):
                tv = input("How many would you like to order?\n")
                self.tv = int(tv)
                stock=self.x.get_stock(5)
                while(stock<self.tv):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num = input("How many would you like to order?\n")
                    self.tv = int(num)
                    stock=self.x.get_stock(5)
                print("\n")

        elif (c_input == 3):
            self.x.display_items("household items")
            print("\n")
            print("1) Cleaner\n")
            print("2) Soap\n")
            print("3) Paper\n")

            item_select3 = input("Which item would you like to order?\n")
            item_select3 = int(item_select3)

            if (item_select3 == 1):

                cleaner = input("How many would you like to order?\n")
                self.cleaner = int(cleaner)
                stock=self.x.get_stock(6)
                while(stock<self.cleaner):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num = input("How many would you like to order?\n")
                    self.cleaner = int(num)
                    stock=self.x.get_stock(6)
                print("\n")

            elif (item_select3 == 2):
                soup = input("How many would you like to order?\n")
                self.soup = int(soup)
                stock=self.x.get_stock(7)
                while(stock<self.soup):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num = input("How many would you like to order?\n")
                    self.soup = int(num)
                    stock=self.x.get_stock(7)
                print("\n")

            elif (item_select3 == 3):
                paper = input("How many would you like to order?\n")
                self.paper = int(paper)
                stock=self.x.get_stock(8)
                while(stock<self.paper):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num = input("How many would you like to order?\n")
                    self.paper = int(num)
                    stock=self.x.get_stock(8)
                print("\n")

        elif (c_input == 4):
            self.x.display_items("toys")
            print("\n")
            print("1) Spider Man\n")
            print("2) Barbie\n")
            print("3) Fidget Spinner\n")

            item_select4 = input("Which item would you like to order?\n")
            item_select4 = int(item_select4)

            if (item_select4 == 1):

                spider_man = input("How many would you like to order?\n")
                self.spider_man = int(spider_man)
                stock=self.x.get_stock(9)
                while(stock<self.spider_man):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num = input("How many would you like to order?\n")
                    self.spider_man = int(num)
                    stock=self.x.get_stock(9)
                print("\n")

            elif (item_select4 == 2):
                barbie = input("How many would you like to order?\n")
                self.barbie = int(barbie)
                stock=self.x.get_stock(10)
                while(stock<self.barbie):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num = input("How many would you like to order?\n")
                    self.barbie = int(num)
                    stock=self.x.get_stock(10)
                print("\n")

            elif (item_select4 == 3):
                fidget_spin = input("How many would you like to order?\n")
                self.fidget_spin = int(fidget_spin)
                stock=self.x.get_stock(11)
                while(stock<self.fidget_spin):
                    print("Only "+str(stock)+" avaible Please enter an appropriate amount")
                    num = input("How many would you like to order?\n")
                    self.fidget_spin = int(num)
                    stock=self.x.get_stock(11)
                print("\n")

   #this function will display the items in the cart
   def view_items(self):
        cart=""
        if(self.comic > 0):
            cart+=str(self.comic)+" Comics in Cart\n"

        if(self.history_book > 0):
            cart+=str(self.history_book)+ " History Booksin Cart\n"

        if(self.cook_book > 0):
            cart+= str(self.cook_book)+ " Cook Books in Cart\n"

        if(self.iphone > 0):
            cart+= str(self.iphone)+ " Iphones in Cart\n"

        if (self.phone_charger > 0):
            cart+=str(self.phone_charger)+ " Phone Chargers in Cart\n"

        if (self.tv > 0):
            cart+= str(self.tv)+" TVs in Cart\n"

        if (self.cleaner > 0):
            cart+= str(self.cleaner)+"Cleaner in Cart\n"

        if (self.soup > 0):
            cart+= str(self.soup)+ " Soup in Cart\n"

        if (self.paper > 0):
            cart+= str(self.paper)+" Paper in Cart\n"

        if (self.spider_man > 0):
            cart+= str(self.spider_man)+" Spider Man Toys in Cart\n"

        if (self.barbie > 0):
            cart+= str(self.barbie)+ " Barbie Toys in Cart\n"

        if (self.fidget_spin > 0):
            cart+= str(self.fidget_spin) +" Fidget Spinner Toys in Cart\n"

        items = self.comic + self.history_book + self.cook_book + self.iphone + self.phone_charger + self.tv \
                + self.cleaner + self.soup + self.paper + self.spider_man + self.barbie + self.fidget_spin
        cart+=str(items)+" Total items"
        #print(cart)
        return cart

    #This function is for giving the option of adding duplicate items
   def add_items(self):
       add_input = input("Would you like to add an? y/n")
       if(add_input == 'y'):
           print("To be done")

    #this function is for calculating the total price of the items
   def total_calc(self):
       total= (self.comic*self.x.get_price(0))+ (self.history_book*self.x.get_price(1))+ (self.cook_book*self.x.get_price(2))
       total+= (self.iphone*self.x.get_price(3))+(self.phone_charger*self.x.get_price(4))+(self.tv*self.x.get_price(5))
       total+= (self.cleaner*self.x.get_price(6))+(self.soup*self.x.get_price(7))+(self.paper*self.x.get_price(8))
       total+= (self.spider_man*self.x.get_price(9))+(self.barbie*self.x.get_price(10))+(self.fidget_spin*self.x.get_price(11))
       return (" Total cost is: $"+str(total)+"\n\n")

   def purchase(self):
       self.x.update_inventory(0,self.comic)
       self.x.update_inventory(1,self.history_book)
       self.x.update_inventory(2,self.cook_book)
       self.x.update_inventory(3,self.iphone)
       self.x.update_inventory(4,self.phone_charger)
       self.x.update_inventory(5,self.tv)
       self.x.update_inventory(6,self.cleaner)
       self.x.update_inventory(7,self.paper)
       self.x.update_inventory(8,self.soup)
       self.x.update_inventory(9,self.spider_man)
       self.x.update_inventory(10,self.barbie)
       self.x.update_inventory(11,self.fidget_spin)
       return

   def empty(self):
       self.comic = 0
       self.history_book = 0
       self.cook_book = 0
       self.iphone = 0
       self.phone_charger = 0
       self.tv = 0
       self.cleaner = 0
       self.paper = 0
       self.soup = 0
       self.spider_man = 0
       self.barbie = 0
       self.fidget_spin = 0
        

    #this function is for giving the option to remove items from the cart
   def remove_items(self):
        print("To be done")

        
#used for testing
def main():

    cart=Store()
    check=1
    while(check==1):
        print("What would you like to do?\n")
        print("1) Select items to purchase\n")
        print("2) View Past Purchases\n")
        print("3) Go to cart\n")
        print("4) Exit store\n")

        user_input = input("Select an option: ")
        user_input = int(user_input)
        print("\n")

        if(user_input == 1):
            cart.select_items()

        elif(user_input == 2):
            print("\n Past Purchases: ")
            file= open("purchases.txt", "r")
            print(file.read())
            file.close()
            print("End of past transactions\n")

        elif(user_input == 3):
            y=cart.view_items()
            print(y)
            print("What would you like to do?\n")
            print("1) purchase the cart\n")
            print("2) return to main menu\n")
            user_input = int(input("Select an option: "))
            if(user_input==1):
                y=cart.view_items()
                u=cart.total_calc()
                t=cart.purchase()
                print(y,u)
                file= open("purchases.txt" , "a")
                file.write(y+u)
                file.close()
                cart.empty()
                
            


        elif(user_input == 4):
            check=0
            #exit()
        else:
            print("Please select an option")
            #main()
    
    #print("Display Items in use")
   #x.display_items("toys")


    #print("Display item in use")
    #x.display_item("toys",2)

    #print("After update_invenotry")
   #x.update_inventory(11,1)
    #x.display_item("toys",2)
    
main()
