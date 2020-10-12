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

   def __init__(self):
       self.select_items()
       self.total_calc()
       self.add_items()
       self.remove_items()
       self.view_items()

    #Function for selecting the category and the items from the category
   def select_items(self):
        x = Inventory()

        print("1) Book\n")
        print("2) Electronics\n")
        print("3) Household Items\n")
        print("4) Toys\n")

        c_input = input("Select a Category: ")
        c_input = int(c_input)
        print("\n")

        if (c_input == 1):
            x.display_items("books")
            print("\n")
            print("1) Comic Book\n")
            print("2) History Book\n")
            print("3) Cooking Book\n")

            item_select1 = input("Which item would you like to order?\n")
            item_select1 = int(item_select1)

            if(item_select1 == 1):

                comic = input("How many would you like to order?\n")
                self.comic = int(comic)

                print("\n")

            elif(item_select1 == 2):
                history_book = input("How many would you like to order?\n")
                self.history_book = int(history_book)

            elif(item_select1 == 3):
                cook_book = input("How many would you like to order?\n")
                self.cook_book = int(cook_book)


        elif (c_input == 2):
            x.display_items("electronics")
            print("\n")
            print("1) Iphone\n")
            print("2) Iphone Charger\n")
            print("3) TV\n")

            item_select2 = input("Which item would you like to order?\n")
            item_select2 = int(item_select2)

            if (item_select2 == 1):

                iphone = input("How many would you like to order?\n")
                self.iphone = int(iphone)

                print("\n")
                print("You have")

            elif (item_select2 == 2):
                phone_charger = input("How many would you like to order?\n")
                self.phone_charger = int(phone_charger)

            elif (item_select2 == 3):
                tv = input("How many would you like to order?\n")
                self.tv = int(tv)

        elif (c_input == 3):
            x.display_items("household items")
            print("\n")
            print("1) Cleaner\n")
            print("2) Soup\n")
            print("3) Paper\n")

            item_select3 = input("Which item would you like to order?\n")
            item_select3 = int(item_select3)

            if (item_select3 == 1):

                cleaner = input("How many would you like to order?\n")
                self.cleaner = int(cleaner)


                print("\n")
                print("You have")

            elif (item_select3 == 2):
                soup = input("How many would you like to order?\n")
                self.soup = int(soup)

            elif (item_select3 == 3):
                paper = input("How many would you like to order?\n")
                self.paper = int(paper)

        elif (c_input == 4):
            x.display_items("toys")
            print("\n")
            print("1) Spider Man\n")
            print("2) Barbie\n")
            print("3) Fidget Spinner\n")

            item_select4 = input("Which item would you like to order?\n")
            item_select4 = int(item_select4)

            if (item_select4 == 1):

                spider_man = input("How many would you like to order?\n")
                self.spider_man = int(spider_man)

                print("\n")
                print("You have")

            elif (item_select4 == 2):
                barbie = input("How many would you like to order?\n")
                self.barbie = int(barbie)

            elif (item_select4 == 3):
                fidget_spin = input("How many would you like to order?\n")
                self.fidget_spin = int(fidget_spin)

   #this function will display the items in the cart
   def view_items(self):
        if(self.comic > 0):
            print(self.comic, "Comics in Cart\n")

        elif(self.history_book > 0):
            print(self.history_book, "History Booksin Cart\n")

        elif(self.cook_book > 0):
            print(self.cook_book, "Cook Books in Cart\n")

        elif(self.iphone > 0):
            print(self.iphone, "Iphones in Cart\n")

        elif (self.phone_charger > 0):
            print(self.phone_charger, "Phone Chargers in Cart\n")

        elif (self.tv > 0):
            print(self.tv, "TVs in Cart\n")

        elif (self.cleaner > 0):
            print(self.cleaner, "Cleaner in Cart\n")

        elif (self.soup > 0):
            print(self.soup, "Soup in Cart\n")

        elif (self.paper > 0):
            print(self.paper, "Paper in Cart\n")

        elif (self.spider_man > 0):
            print(self.spider_man, "Spider Man Toys in Cart\n")

        elif (self.barbie > 0):
            print(self.barbie, "Barbie Toys in Cart\n")

        elif (self.fidget_spin > 0):
            print(self.fidget_spin, "Fidget Spinner Toys in Cart\n")

        items = self.comic + self.history_book + self.cook_book + self.iphone + self.phone_charger + self.tv \
                + self.cleaner + self.soup + self.paper + self.spider_man + self.barbie + self.fidget_spin

        print(items, "total items")

    #This function is for giving the option of adding duplicate items
   def add_items(self):
       add_input = input("Would you like to add an? y/n")
       if(add_input == 'y'):
           print("To be done")

    #this function is for calculating the total price of the items
   def total_calc(self):
        print("Bean")

    #this function is for giving the option to remove items from the cart
   def remove_items(self):
        print("To be done")

        
#used for testing
def main():

    cart=Store()

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
        print("TBA - Purchase History")

    elif(user_input == 3):
        cart.view_items()


    elif(user_input == 4):
        exit()
    else:
        print("Please select an option")
        main()
    
    #print("Display Items in use")
   #x.display_items("toys")


    #print("Display item in use")
    #x.display_item("toys",2)

    #print("After update_invenotry")
   #x.update_inventory(11,1)
    #x.display_item("toys",2)
    
main()
