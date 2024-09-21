menu = """
            WELCOME TO PYTHON BANK MANAGEMENT SYSTEM

            SELECT YOUR ROLE 

            1) Banker

            2) Customer

            3) Exit
"""
banker_menu= """            

            1) Add customer
            2) view customer 
            3) view all customer 
            4) Total amount in bank

"""
customer_menu="""
                Welcome to customer App

                operation menu:
                1) withdraw Amount
                2) Depsosit Amount
                3) view balance
"""
print(menu)
b ={}
banker=input("Choose your role : ")     
status= True
while status:
    if banker=="Banker":   
     print(banker_menu)
     a = int(input("Enter operation which u want to perform :"))
     if a == 1:
         account = int(input("Enter account Number : "))
         name = input("Enter customer name : ")
         balance = int(input("Enter opening balance : "))
         b[account,name,balance]=a
         c = input("Do u want to perform more operation press Y for yes and N for No") .lower()
         if c =="y" or c == "yes":
             status=True
         else:
           status=False   
    elif a ==2:
            print(b)
    elif banker=="Customer":
       print(customer_menu)
       d = int(input("Enter the operation u want to perform : "))
       if d == 1:
          e  = int(input("Enter the amount u want to withdraw : "))
          f = balance-e
          print("Your balance is ",f)
       elif d == 2:
          g = int(input("Enter the amount u want to deposit : "))
          h = balance+g
       elif d == 3 :
          print("Your total Balance is ",h)

    elif  a==3:
       break
