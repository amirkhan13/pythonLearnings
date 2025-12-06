num1 =int(input("Enter First number to calculate:"))
operator =input("Enter the Operator eg. +,-,*,/:")
num2 =int(input("Enter Second numbers to calculate:"))


def calculate():
    if(operator =="+"):
     ans =num1 + num2
     print(f"The addition of the two numbers is {ans}")

    elif(operator=="-"):
       ans =num1 - num2
       print(f"The Subtraction of the two numbers is {ans}")
    elif(operator=="*"):
       ans =num1 * num2
       print(f"The Multiplication of the two numbers is {ans}")

    elif(operator=="/"):
      if(num2 ==0):
         print("Cannot Divide a number by Zero inccorect Operation!!")
      else:
        ans =num1 / num2
        print(f"The Division of the two numbers is {ans}")
    else:
       print("Invalid Operator Enter the correct operator")
       
calculate()




