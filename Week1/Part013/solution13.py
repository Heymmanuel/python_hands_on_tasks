print("Hello costumer! welcome to your cost calculator: ")
print()
user_input1 = int(input("How many days will you stay?: "))
user_input2 = int(input("How much does the hotel cost per night: "))
user_input3 = int(input("How much does your flight cost?: "))
user_input4 = int(input("Enter price if you need a rental ride, (enter 0 if you don't need): "))

hotel_cost = user_input2 * user_input1
total_cost = hotel_cost + user_input3 + user_input4
print(f'Your total cost is, ${total_cost: .2f}')
