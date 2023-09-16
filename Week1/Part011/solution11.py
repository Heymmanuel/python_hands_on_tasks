def max_min(numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    return max_value, min_value


input_numbers = []
while True:
    user_input = input("Enter a number (or 'done' when you are finished): ")
    if user_input.lower() == 'done':
        break

    try:
        number = float(user_input)
        input_numbers.append(number)
    except ValueError:
        print("Please enter a valid number")


max_val, min_value = max_min(input_numbers)
print(f'Maximum value: {max_val} and minimum value: {min_value}')