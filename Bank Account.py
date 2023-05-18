#This is program of an ATM simulation
#It allows the user to access its account
#Check his balance
#Make withdrawals and deposits to his account
#And exit from it after making transactions

#This function is created to display the options available in the ATM
def displayMenu():
    print("\n1- Blance Inquiry")
    print("2- Withdraw")
    print("3- Deposit")
    print("4- Exit")

#This function is created to make withdrawals from the user's account
def withdraw(balance):
    amount = int(input("Enter an amount to withdraw: "))
    while(amount>balance):
        amount = int(input("Insufficient Account balance! Enter again: "))
    balance = balance - amount
    print("Your amount has been Withdrawn!")
    return balance

#This function is created to make deposits to the user's account
def deposit(balance):
    amount = int(input("Enter an amount to deposit: "))
    while (amount < 0):
        amount = int(input("Amount can't be less than 0! Enter again: "))
    balance = balance + amount
    print("Your amount has been Deposited!")
    return balance

#The main function as the point of entry
def main():
    #Initializing the variables
    balance = 1000
    pin = "1111"

    #Taking user's input
    user_pin = input("Enter your pin: ")

    if user_pin != pin:
        print("Wrong Pin!")
    else:
        choice = 1

        #looping through the options until user exits the program
        while choice != 4:
            displayMenu() #Displaying Menu options

            #Taking user input
            choice = int(input("Enter your choice: "))

            #Performing functionalities according to the user's input
            if choice == 1:
                print("Your Balance is: ", balance)
            elif choice == 2:
                balance = withdraw(balance)
            elif choice == 3:
                balance = deposit(balance)
            elif choice == 4:
                print("Thank you for using our services!")
            else:
                print("Invalid Input!")

if __name__ == '__main__':
    main()