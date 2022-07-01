while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
 
 
  def select_op(choice):
        operation = "+,-,*,/,^,%,#,$"
        if (choice in operation):
            if(choice == '#'):
            #program ends here
                print("Done. Terminating")
                exit()
           
            #Adding
            elif(choice == '+'):
                try:
                    num1 = input("Enter first number: ")
                    print (num1)
                    n1 = int(num1)
                    num2 = input("Enter second number: ")
                    print (num2)
                    n2 = int(num2)
                    adding = n1 + n2
                    print(float(num1),"+",float(num2),"=", float(adding))
                except ValueError:
                    pass
               
            #Dividing
            elif(choice == '/'):
                try:
                    num1 = input("Enter first number: ")
                    print (num1)
                    n1 = int(num1)
                    num2 = input("Enter second number: ")
                    print (num2)
                    n2 = int(num2)
                    dividing = n1 / n2
                    print (float(num1),"/",float(num2),"=",float(dividing))
       
                except ZeroDivisionError:
                    print ("float division by zero")
                    print (float(num1),"/",float(num2),"=","None")
                except ValueError:
                    pass
               
            #Substraction
            elif (choice == '-'):
                try:
                    num1 = input("Enter first number: ")
                    print (num1)
                    n1 = int(num1)
                    num2 = input("Enter second number: ")
                    print (num2)
                    n2 = int(num2)
                    sub = n1 - n2
                    print (float(num1),"-",float(num2),"=",float(sub))
                     
                except ValueError:
                    print("Done. Terminating")
                    exit()
                   
            #Multplication
            elif(choice == '*'):
                try:
                    num1 = input("Enter first number: ")
                    print (num1)
                    n1 = int(num1)
                    num2 = input("Enter second number: ")
                    print (num2)
                    n2 = int(num2)
                    Multplication = n1 * n2
                    print(float(num1),"*",float(num2),"=", float(Multplication))
                except ValueError:
                    pass
               
               
            #Power
            elif(choice == '^'):
                try:
                    num1 = input("Enter first number: ")
                    print (num1)
                    n1 = int(num1)
                    num2 = input("Enter second number: ")
                    print (num2)
                    n2 = int(num2)
                    Power = n1 ** n2
                    print(float(num1),"^",float(num2),"=", float(Power))
                except ValueError:
                    pass
               
            #Remainder
            elif(choice == '%'):
                try:
                    num1 = input("Enter first number: ")
                    print (num1)
                    n1 = int(num1)
                    num2 = input("Enter second number: ")
                    print (num2)
                    n2 = int(num2)
                    Remainder = n1 % n2
                    print(float(num1),"%",float(num2),"=", float(Remainder))
                except ValueError:
                    pass
               
               
        else:
            print ("Unrecognized operation")
     

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  select_op(choice)
