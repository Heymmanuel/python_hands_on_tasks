def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except(ValueError, TypeError):
        print("Error, please enter numeric input")
        return False


input_number = []
while True:
    p_input = input("Enter a number (or 'done' when you are finished): ")
    if p_input.lower() == 'done':
        break
    num = check_for_float(p_input)
    input_number.append(num)


max_value = max(input_number)
min_value = min(input_number)

print(f'Maximum number: {max_value}, Minimum number: {min_value}')

