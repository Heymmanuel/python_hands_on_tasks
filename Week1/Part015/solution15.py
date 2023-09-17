user_input1 = int(input("What is your monthly salary?: "))
if user_input1 >= 2000:
    print(f'You are eligible for mortgage')
else:
    print(f"You are not eligible for mortgage")

user_input2 = int(input("What is your credit score?: "))
if user_input2 >= 800:
    print('Your interest rate is 4%')
elif user_input2 >= 750:
    print('Your interest rate is 6%')
elif user_input2 < 750:
    print('Your interest rate is 5%')

user_input3 = input("Please specify if you have any disabilities? (Yes or No): ")
if user_input3.lower() != 'no':
    print('Congratulations you have been discounted, your interest rate is now 4%')
    exit()
