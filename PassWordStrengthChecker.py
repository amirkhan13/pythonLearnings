password = input("Enter a password to check the strength: ")

def CheckPWD():
    score =0
    for char in password:
        if char.isupper():
            score +=1
          
        if char.islower():
            score+=1
           
        if char.isdigit():
            score+=1
            
        if not char.isalnum():
            score+=1
          
        
    if(score >=4):
        print("Your password is strong")
    elif(score ==3):
        print("Your password Strength is Average")
    else:
        print("Your password is weak")

CheckPWD()