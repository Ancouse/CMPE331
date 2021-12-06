#CMPE 331 -Worksheet3
#Oğuz Mete Kara- 118200071
#Sedanur Çifçi - 118200056

#Firsly, We need to send a message to work.

#Seda -> I wrote list for user.
#Mete -> I added step 5 and 6
Calculate_list= ("""
a
Hello User,Choose a calculating,
press "1" for  sum,
press "2" for  subtract,
press "3" for  devide,
press "4" for  multiply,
press "5" for show list,
press "6" for quit,

""")
print(Calculate_list)
#Seda -> I used "try" block in this step because if there is a problem , user can show it.
try:
    #I used "while" block  because user can be use again.
    while True:

        method = str(input("Choose a calculating: "))
        # Mete -> I used "if" method here because if user presses 5, user should not see number 1 and number2.
        if method !="5" and method !="6":
            number1 = int(input("First Number: "))
            number2 = int(input("Second Number: "))
        #Seda -> I wrote methods.
        if method == "1":
            print(number1 + number2)
            print("Nice job,Show list press '5' leave with press '6'\n ")
        elif method == "2":
            print(number1 - number2)
            print("Nice job,Show list press '5' leave with press '6'\n ")
        elif method == "3":
            print(number1 / number2)
            print("Nice job,Show list press '5' leave with press '6'\n ")
        elif method =="4":
            print(number1 * number2)
            print("Nice job,Show list press '5' leave with press '6'\n ")
        elif method == "5":
            print(Calculate_list)
        elif method =="6":
            print("Have a nice day")
            break
except:
    print("Somethings are wrong")
