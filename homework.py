bill = float(input("Enter the total bill: "))
due = bill

while True:
    print("Your due amount is:", due)
    pay = float(input("Enter amount to pay: "))

    if pay >= due:
        print("Bill is paid.")
        due = 0
        break
    else:
        due = due - pay
        print("Remaining due:", due)

print("Thank you")
