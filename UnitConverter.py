
def Convert_Centimerters_to_meters():
    
    num = int(input("Enter the Number to Convert:"))

    print("----CHOICES---")
    print("1.Do you want convert to cm to m")
    print("2.Do you want convert to m to cm")


    choice = input("Enter the choice:")

    if choice =="1":
        ans = num/100
        print(f"Converted:{num} cm into {ans} m")
    elif choice =="2":
        ans =num*100
        print(f"Converted:{num} m into {ans} cm")

    else:
        print("Invalid Choice please try again!!")


def Convert_Kgs_to_grams():

    num = int(input("Enter the Number to Convert:"))

    print("----CHOICES---")
    print("1.Do you want convert to g to kgs")
    print("2.Do you want convert to kgs to g")

    choice = input("Enter the choice:")

    if choice =="1":
        ans = num/1000
        print(f"Converted:{num} gs into {ans} kg")
    elif choice =="2":
        ans =num*1000
        print(f"Converted:{num} kgs into {ans} gs")

    else:
        print("Invalid Choice please try again!!")



def Convert_Days_to_Seconds():

    num = int(input("Enter the Number to Convert:"))

    print("----CHOICES---")
    print("1.Do you want to convert days to secs")
    print("2.Do you want to convert secs to days")

    choice =input("Enter the Choice:")

    if choice =="1":
        ans = num*60*60*24
        print(f"Converted:{num} days into {ans} secs")
    elif choice =="2":
        minutes= num/60
        hours=minutes/60
        days=hours/24
        print(f"Converted:{num} secs into {days} days")

    else:
        print("Invalid Choice please try again!!")



def main():

    while True:
        print("--select what you want to convert:")
        print("1. Convert Cm to m,vice versa")
        print("2. Convert kgs to gs,vice versa")
        print("3. Convert days to secs,vice versa")
        print("4. Exit")

        choice = input("Enter your choice:")

        if choice =="1":

         Convert_Centimerters_to_meters()   

        elif choice =="2":
            Convert_Kgs_to_grams()
        
        elif choice=="3":
            Convert_Days_to_Seconds()
        
        elif choice=="4":
            break
        else:
            print("Invalid Choice Try again!!!")


main()