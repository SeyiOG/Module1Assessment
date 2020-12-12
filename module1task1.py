#OGRILL Application
#introductory messages displayed below
print(" ~~~~~~~~~~~~~~~~~~~~~~~ ")
print("|    OGRILL    |")
print("|    Ordering System    |")
print(" ~~~~~~~~~~~~~~~~~~~~~~~ ")
print("")
print("Welcome to our takeway ordering system.")

from datetime import date #import date
firstname = input("enter your firstname: ") #user enters firstname 
middlename = input("enter your middlename: ") #user enters middlename
lastname = input("enter your lastname: ") #user enters lastname
userdetails = [firstname, middlename, lastname] #create the userdetails list
#format customer name
customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
address = input("enter your address: ") #user enters address
thedate = date.today() #save today's date as "thedate"
file = open("menu.txt","r") #open the menu file

totalcost = 0
code = input("Enter the option code you would like to order: (e.g.P1)") #user enters the code they want to order from the menu
#code = ordercode.upper() #format the ordercode in upper case
print("Type X to exit") #Display type x to exit

while(code != "X"):
    for line in file:
        data = line.split(";") #data in menu file is separated by ;
        itemcode = data[0] # item code is the first item on the line
        itemdesc = data[1] # item description is the second item on the line 
        itemprice = float(data[2]) # item price is the 3rd item on the line
        if (code == itemcode): # for every item code
            print(itemcode + "-" + itemdesc + '- #' + str(itemprice)) # print the itemcode, description and price
            totalcost = totalcost + itemprice #total cost
    code = input("Enter another code or type X to exit: ")

print("order processing")
if totalcost == 0:
    delivery = 0
elif totalcost >=7000:
    delivery = 0
elif totalcost < 7000:
    delivery = 1500
ordertotal = delivery + totalcost

print("Here is your receipt: ")
print("%s\nAddress: %s\nDate: %s\nOrder Total: #%s\n"%(customername, address, str(thedate), str(ordertotal)))    
print("Goodbye!")
file.close()