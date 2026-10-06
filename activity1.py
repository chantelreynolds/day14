def calculate_change(paid, price):
    change = paid-price
    return change

snack_price = 50
print("the snack cost is ", snack_price)
print("accepted coins are 5, 10, or 25 \n")

total_inserted = 0
coins_inserted = 0

while True :
    coin = int(input("Insert a coin 5, 10, or 25 "))

    #using continue keyword
    if coin != 5 and coin != 10 and coin != 25 :
        print("Invalid coin try again \n")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"inserted {coin}. total so far : {total_inserted}\n")

    #using break keyword
    if total_inserted >= snack_price :
        print("enough money inserted\n")
        break

change_due = calculate_change(total_inserted, snack_price)
print("dispensing your snack ...")

#using pass keyword
if change_due == 0 :
    pass
else:
    print("Here is your change amount ", change_due)

print("Purchase summary")
print("Snack price is ", snack_price)
print("Coins inserted ", coins_inserted)
print("Total paid amount ", total_inserted)
print("Change given ", change_due)
print("THANK YOU FOR YOUR PURCHASE!")



