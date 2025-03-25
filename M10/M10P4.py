total_ticket_price = 0
repeat = input("Do you want to calculate a train ticket price? (Yes or No): ")
while repeat.lower() == "yes":
        last_name = input("Enter last name: ")
        miles = int(input("Enter miles from downtown Chicago: "))
        if miles >= 30:
            ticket_price = 12
        elif miles >= 20:
            ticket_price = 10
        elif miles >= 10:
            ticket_price = 8
        else:
            ticket_price = 5

        total_ticket_price += ticket_price
        print("Ticket price for", last_name, "is:", ticket_price)
        print()
        repeat = input("Do you want to calculate a train ticket price? (Yes or No): ")

print("Total of all train ticket prices is:", total_ticket_price)