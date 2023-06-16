weight_p = eval(input("Enter your weight in pounds: "))
height_i = eval(input("Enter your height in inches: "))

weight_kg = weight_p * 0.45359237
height_meters = height_i * 0.0254

BMI = weight_kg / (height_meters ** 2)

print("Your BMI is:",BMI )