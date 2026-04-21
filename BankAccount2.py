import BankAccount

def main():
    start_bal = float(input('Enter starting balance: '))
    savings = BankAccount.bank_account(start_bal)

    pay = float(input('How much were you paid this week? '))
    print("I will deposit that into your account. ")
    savings.deposit(pay)

    print(f"Your accountbalance is ${savings.get_balance():,.2f}.")

if __name__ == "__main__":
    main()