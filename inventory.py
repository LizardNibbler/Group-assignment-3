#used to include the item classes
from item import *


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

        
#used for testing
def main():
    x=Inventory()
    
    print("Display Items in use")
    x.display_items("toys")

    
    print("Display item in use")
    x.display_item("toys",2)

    print("After update_invenotry")
    x.update_inventory(11,1)
    x.display_item("toys",2)
    
main()
