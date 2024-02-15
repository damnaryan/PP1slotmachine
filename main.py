# SINCE THIS IS A LEARNING PROJECT, NOTES ARE MADE FOR WHAT EACH COMMAND DOES.

MAX_DEPOSIT = 1000
MAX_BET = 100
MIN_BET = 1

# Here, we are defining a fuction to take the deposit from the user before staring the game.
def deposit():
# 'def' is used to define a function in python. And the complete cmd looks like this *def fuction():*.
    while True:
# 'while' loops are used to create undefined or user dependent loops.
        amount = input("Enter the amount you want to deposit? $")
# Now, we have to make sure that the input is a integer and not string or something.
        if amount.isdigit():
            amount = int(amount)
#Chekcing if the number is greater than 0.
            if amount > 0:
                break
            else: 
                print("amount must be greater than 0.")
        else:
            print("Enter a valid number.")
    
    return amount

def get_bet():
    while True:
        bet = input("Enter the amount you have to bet: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else: 
                print(f"Betting amount should be between ${MIN_BET} - {MAX_BET}.")
        else:
            print("Enter a valid numeber.")
    return bet

def main():
    balance = deposit()

main()

#Defining a function does not runs the fuction, on executing the program. A fuction only runs when it is called.
    
