user_num = input("Enter two numbers separated by a commma: ")

user_input = user_num.split(",")

num1, num2 = map(float, user_input)
sum = num1 + num2

print(f'Sum of {num1} and {num2} is {sum}')