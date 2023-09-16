user_days = int(input("Enter days: "))

years = user_days // 365
print(f'YEARS: {years}')

weeks = (user_days - (years * 365)) // 7
print(f'WEEKS: {weeks}')

days_remaining = user_days - ((years * 365) + (weeks * 7))
print(f'DAYS: {days_remaining}')