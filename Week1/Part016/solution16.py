def bmiCalculator():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)
    if bmi <= 18.4:
        print("Hello friend! You are underweight.")
    if bmi >= 18.4 and bmi < 25:
        print("Hello friend! Your weight is normal.")
    if bmi >= 25 and bmi < 30:
        print("Hello friend! Your weight is overweight.")
    if bmi >= 30 and bmi <= 35:
        print("Hello friend! You are obese.")


bmiCalculator()
