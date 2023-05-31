// Program to simulate an ATM machine
public class ATM{

    @Override
	public String toString() {
		return "ATM []";
	}

	// function to display menu
    public static void displayMenu(){
        System.out.println("\n1. Check Balance");
        System.out.println("2. Withdraw");
        System.out.println("3. Deposit");
        System.out.println("4. Exit");
    }

    // function to withdraw money
    public static int withdraw(int balance){
        System.out.println("Enter amount to withdraw: ");
        int amount = Integer.parseInt(System.console().readLine());
        while(amount > balance){
            System.out.println("Insufficient Balance. Enter amount again: ");
            amount = Integer.parseInt(System.console().readLine());
        }
        balance -= amount;
        System.out.println("Your balance has been withdrawn!");
        return balance;
    }

    // function to deposit money
    public static int deposit(int balance){
        System.out.println("Enter amount to deposit: ");
        int amount = Integer.parseInt(System.console().readLine());
        while(balance<0){
            System.out.println("Invalid amount! Enter again: ");
            amount = Integer.parseInt(System.console().readLine());
        }
        balance += amount;
        System.out.println("Your balance has been deposited!");
        return balance;
    }

    // main function
    public static void main(final String[] args){

        // initializing the variables
        int balance = 100;
        final int pin = 1111;
        
        // taking user input
        int userPin;
        System.out.println("Enter you pin: ");
        userPin = Integer.parseInt(System.console().readLine());

        // validating user input
        while(userPin != pin){
            System.out.println("Wrong pin! Enter again: ");
            userPin = Integer.parseInt(System.console().readLine());
        }

        if(userPin == pin){
            int choice = 1;
            
            // displaying menu
            while(choice!=4){
                displayMenu();

                // taking user choice
                System.out.println("Enter your choice: ");
                choice = Integer.parseInt(System.console().readLine());

                if(choice==1){
                    System.out.println("Your balance is: "+balance);
                }
                else if(choice==2){
                    balance = withdraw(balance);
                }
                else if(choice == 3){
                    balance = deposit(balance);
                }
                else if(choice == 4){
                    System.out.println("Thank you for using our services!");
                }
                else{
                    System.out.println("Invalid Input!");
                }

            }

        }

    }
}