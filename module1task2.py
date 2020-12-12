#ZCB Account Registration App


import random
nubanaccts = (random.sample(range(1000000000, 2999999999), 1000)) #generate the list of account numbers
firstname = input("enter your firstname: ") #user enters firstname 
middlename = input("enter your middlename: ") #user enters middlename
lastname = input("enter your lastname: ") #user enters lastname
phonenumber = input("enter your phonenumber: +234 ") #enter phone number in internatiional format and store as phonenumber
address = input("enter your address: ") #user enters address
sphoneno = str(phonenumber) #convert phone number to string
depositamt = int(input("enter amount to deposit: ")) #user specifies the deposit amount
nubanaccts = tuple(nubanaccts) #convert the nubanaccts list to a tuple
promocodes = ["SOROSOKE1TIME", 'SPEAKUP2DAY', 'JESUS4EVER', 'J1MASUN']
accbal = int(depositamt) #opening account balance is equal to deposit amount

age = int(input("How old are you? "))
if (age >= 18):
    print ("Age requirement met")
    if (depositamt >= 1000):      #if deposit amount is greater than 1000
            print("You are eligible to open an account") #display message in bracket
            accbal = int(depositamt) #opening account balance is equal to deposit amount
            print("Do you have a Promo Code") #display message in bracket
            codecheck = input("Yes/No: ")  #user confirms availability of promo code
            fcodecheck = codecheck[0].upper() #format codecheck as specified
            if fcodecheck == "Y": #if user has a promo code
                promocode = input("enter promo code: ") #enter promo code
                fpromo = promocode.upper() #format promo code
                for pcode in promocodes:  #for valid promo code
                    if (pcode == fpromo): #if code is correct
                        accbal = accbal + 500  #user is credited with 500 naira
                        saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                        accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                        saccnum = str(accountnum)
                        userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                        customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                        phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                        accno = "Account Number: "+saccnum #assign the customer a nuban number
                        dage = "Age: " + str(age) #format the age
                        ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                        ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                        print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                    elif (pcode != fpromo): #if code is not correct
                        print("Please enter VALID Promo Code (Final Attempt)") #print message displayed 
                        promocode = input("enter promo code: ") #enter promo code
                        fpromo = promocode.upper() #format promo code
                        for pcode in promocodes:  #for valid promo code
                            if (pcode == fpromo): #if code is correct
                                accbal = accbal + 500  #user is credited with 500 naira
                                saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                                accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                                saccnum = str(accountnum)
                                userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                                customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                                phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                                accno = "Account Number: "+saccnum #assign the customer a nuban number
                                dage = "Age: " + str(age) #format the age
                                ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                                ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                                print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                            else:
                                accbal = accbal + 0       #account balance stays the same
                                saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                                accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                                saccnum = str(accountnum)
                                userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                                customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                                phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                                accno = "Account Number: "+saccnum #assign the customer a nuban number
                                dage = "Age: " + str(age) #format the age
                                ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                                ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                                print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                        break
            elif fcodecheck != "Y":    #if user doesn't have a promo code
                accbal = accbal + 0       #account balance stays the same
                saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                saccnum = str(accountnum)
                userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                accno = "Account Number: "+saccnum #assign the customer a nuban number
                dage = "Age: " + str(age) #format the age
                ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
    elif (depositamt < 1000):     #if deposit amount is less than 1000
        print("you need to deposit at least 1000")  #display message in bracket
        print("will you be increasing the deposit amount?")  #display message in bracket
        depincr = input("Yes/No: ") #user inputs yes or no
        fdepincr = depincr[0].upper() #format to upper case of first letter
        if (fdepincr == "Y"):
            depositamt = int(input("enter amount to deposit: ")) #user specifies the deposit amount
            if (depositamt >= 1000):
                print("You are eligible to open an account") #display message in bracket
                accbal = int(depositamt) #opening account balance is equal to deposit amount
                print("Do you have a Promo Code") #display message in bracket
                codecheck = input("Yes/No: ")  #user confirms availability of promo code
                fcodecheck = codecheck[0].upper() #format codecheck as specified
                if fcodecheck == "Y": #if user has a promo code
                    promocode = input("enter promo code: ") #enter promo code
                    fpromo = promocode.upper() #format promo code
                    for pcode in promocodes:  #for valid promo code
                        if (pcode == fpromo): #if code is correct
                            accbal = accbal + 500  #user is credited with 500 naira
                            saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                            accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                            saccnum = str(accountnum)
                            userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                            customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                            phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                            accno = "Account Number: "+saccnum #assign the customer a nuban number
                            dage = "Age: " + str(age) #format the age
                            ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                            ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                            print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                        elif (pcode != fpromo): #if code is not correct
                            print("Please enter VALID Promo Code (Final Attempt)") #print message displayed 
                            promocode = input("enter promo code: ") #enter promo code
                            fpromo = promocode.upper() #format promo code
                            for pcode in promocodes:  #for valid promo code
                                if (pcode == fpromo): #if code is correct
                                    accbal = accbal + 500  #user is credited with 500 naira
                                    saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                                    accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                                    saccnum = str(accountnum)
                                    userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                                    customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                                    phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                                    accno = "Account Number: "+saccnum #assign the customer a nuban number
                                    dage = "Age: " + str(age) #format the age
                                    ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                                    ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                                    print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                                else:
                                    accbal = accbal + 0       #account balance stays the same
                                    saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                                    accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                                    saccnum = str(accountnum)
                                    userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                                    customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                                    phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                                    accno = "Account Number: "+saccnum #assign the customer a nuban number
                                    dage = "Age: " + str(age) #format the age
                                    ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                                    ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                                    print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                            break
                elif fcodecheck != "Y":    #if user doesn't have a promo code
                    accbal = accbal       #account balance stays the same
                    saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                    accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                    saccnum = str(accountnum)
                    userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                    customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                    phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                    accno = "Account Number: "+saccnum #assign the customer a nuban number
                    dage = "Age: " + str(age) #format the age
                    ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                    ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                    print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
            elif (depositamt < 1000):
                print("You cannot open an account\nDeposit amount not sufficient")
        else:
            print("You cannot open an account\nDeposit amount not sufficient")   
elif (age < 18):
    print("Provide ID of parent or guardian")
    pgid  = input("Is parent/guardian ID available?(Y/N): ")
    fpgid = pgid[0].upper() #format to upper case of first letter
    if (fpgid == "Y"):   #if parent/guardian ID is available
        print("ID requirement met")   #print ID requirement met
        if (depositamt >= 1000):      #if deposit amount is greater than 1000
            print("You are eligible to open an account") #display message in bracket
            accbal = int(depositamt) #opening account balance is equal to deposit amount
            print("Do you have a Promo Code") #display message in bracket
            codecheck = input("Yes/No: ")  #user confirms availability of promo code
            fcodecheck = codecheck[0].upper() #format codecheck as specified
            if fcodecheck == "Y": #if user has a promo code
                promocode = input("enter promo code: ") #enter promo code
                fpromo = promocode.upper() #format promo code
                for pcode in promocodes:  #for valid promo code
                    if (pcode == fpromo): #if code is correct
                        accbal = accbal + 500  #user is credited with 500 naira
                        saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                        accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                        saccnum = str(accountnum)
                        userdetails = [firstname, middlename, lastname, sphoneno, age,] #create the userdetails list
                        customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                        phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                        accno = "Account Number: "+saccnum #assign the customer a nuban number
                        dage = "Age: " + str(age) #format the age
                        ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                        ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                        print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                    elif (pcode != fpromo): #if code is not correct
                        print("Please enter VALID Promo Code (Final Attempt)") #print message displayed 
                        promocode = input("enter promo code: ") #enter promo code
                        fpromo = promocode.upper() #format promo code
                        for pcode in promocodes:  #for valid promo code
                            if (pcode == fpromo): #if code is correct
                                accbal = accbal + 500  #user is credited with 500 naira
                                saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                                accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                                saccnum = str(accountnum)
                                userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                                customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                                phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                                accno = "Account Number: "+saccnum #assign the customer a nuban number
                                dage = "Age: " + str(age) #format the age
                                ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                                ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                                print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                            else:
                                accbal = accbal + 0       #account balance stays the same
                                saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                                accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                                saccnum = str(accountnum)
                                userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                                customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                                phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                                accno = "Account Number: "+saccnum #assign the customer a nuban number
                                dage = "Age: " + str(age) #format the age
                                ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                                ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                                print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                        break
            elif fcodecheck != "Y":    #if user doesn't have a promo code
                accbal = accbal       #account balance stays the same
                saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                saccnum = str(accountnum)
                userdetails = [firstname, middlename, lastname, sphoneno, age,] #create the userdetails list
                customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                accno = "Account Number: "+saccnum #assign the customer a nuban number
                dage = "Age: " + str(age) #format the age
                ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
        elif (depositamt < 1000):     #if deposit amount is less than 1000
            print("you need to deposit at least 1000")  #display message in bracket
            print("will you be increasing the deposit amount?")  #display message in bracket
            depincr = input("Yes/No: ") #user inputs yes or no
            fdepincr = depincr[0].upper() #format to upper case of first letter
            if (fdepincr == "Y"):
                depositamt = int(input("enter amount above 1000 to deposit: ")) #user specifies the deposit amount
                if depositamt > 1000:
                    print("You are eligible to open an account") #display message in bracket
                    accbal = int(depositamt) #opening account balance is equal to deposit amount
                    print("Do you have a Promo Code") #display message in bracket
                    codecheck = input("Yes/No: ")  #user confirms availability of promo code
                    fcodecheck = codecheck[0].upper() #format codecheck as specified
                    if fcodecheck == "Y": #if user has a promo code
                        promocode = input("enter promo code: ") #enter promo code
                        fpromo = promocode.upper() #format promo code
                        for pcode in promocodes:  #for valid promo code
                            if (pcode == fpromo): #if code is correct
                                accbal = accbal + 500  #user is credited with 500 naira
                                saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                                accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                                saccnum = str(accountnum)
                                userdetails = [firstname, middlename, lastname, sphoneno, age,] #create the userdetails list
                                customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                                phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                                accno = "Account Number: "+saccnum #assign the customer a nuban number
                                dage = "Age: " + str(age) #format the age
                                ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                                ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                                print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                            elif (pcode != fpromo): #if code is not correct
                                print("Please enter VALID Promo Code (Final Attempt)") #print message displayed 
                                promocode = input("enter promo code: ") #enter promo code
                                fpromo = promocode.upper() #format promo code
                                for pcode in promocodes:  #for valid promo code
                                    if (pcode == fpromo): #if code is correct
                                        accbal = accbal + 500  #user is credited with 500 naira
                                        saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                                        accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                                        saccnum = str(accountnum)
                                        userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                                        customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                                        phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                                        accno = "Account Number: "+saccnum #assign the customer a nuban number
                                        dage = "Age: " + str(age) #format the age
                                        ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                                        ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                                        print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                                    else:
                                        accbal = accbal + 0       #account balance stays the same
                                        saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                                        accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                                        saccnum = str(accountnum)
                                        userdetails = [firstname, middlename, lastname, sphoneno, age] #create the userdetails list
                                        customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                                        phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                                        accno = "Account Number: "+saccnum #assign the customer a nuban number
                                        dage = "Age: " + str(age) #format the age
                                        ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                                        ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                                        print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                                break
                    elif fcodecheck != "Y":    #if user doesn't have a promo code
                        accbal = accbal       #account balance stays the same
                        saccbal = "Acc. Balance: "+ str(accbal) #format account balance
                        accountnum = nubanaccts[random.randint(1,999)] #assign an account number to the customer from the nuban tuple
                        saccnum = str(accountnum)
                        userdetails = [firstname, middlename, lastname, sphoneno, age,] #create the userdetails list
                        customername = "Customer Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' 
                        phoneno = "Phone No.: 0" + userdetails[3] #retrieve phone number from the userdetails list
                        accno = "Account Number: "+saccnum #assign the customer a nuban number
                        dage = "Age: " + str(age) #format the age
                        ass2file = open("mod1tsk2out.txt", "w+") #open ass3out text file
                        ass2file.write("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))#write the customer name, phone number and account number to a text file
                        print("%s\n%s\n%s\n%s\n%s"%(customername, dage, phoneno, accno, saccbal))
                elif depositamt < 1000:
                    print("You cannot open an account\nDeposit amount not sufficient") 
            else:
                print("You cannot open an account\nDeposit amount not sufficient") 
    elif (fpgid != "Y"):
        print("You cannot open an account")
        print("Get a valid parent/guardian ID\nGoodbye")