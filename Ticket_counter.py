tickets = {
    "1" : ("Spiderman Brand New Day" , 850),
    "2" : ("Avengers Doomsday" , 650) ,
    "3" : ("Batman" , 450),  
    "4" : ("Punisher", 550)        
}

no_tickets = 0
print("-----------Movies-----------Ticket Price---------")
for sr_no, movie in tickets.items():
    print(f"{sr_no}.{movie[0]:25}  ${movie[1]:.2f}")
print("-------------------------------------------------")

while True:
    sr_no = input("Enter serial number of the Movie You want to watch: ")
    if sr_no in tickets:
        break
    else:
        print("Invalid number! Please Enter Valid Number.")
no_tickets = int(input("Enter No of tickets you want to watch:"))
total = tickets[sr_no][1] * no_tickets
if no_tickets > 0:
    print(f"For {tickets[sr_no][0]} your total cost is ${total}")
else:
    print("Enter Valid! no of tickets")

