def perform_transaction():
    amt_due = 50
    accepted_denominations = [5,10,25]
    while True:
        if amt_due == 0:
            print("Change Owed: 0")
            break
        else:
            if amt_due < 0:
                print(f"Change Owed: {abs(amt_due)}")
                break
            else:
                print(f"Amount Due: {amt_due}")
                user_insert = int(input("Insert Coin: "))
                if user_insert in accepted_denominations:
                    amt_due -= user_insert
        



def main():
    perform_transaction()


main()