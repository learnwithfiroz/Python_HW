hight=float(input("Enter Your Hight: "))
weight=float(input("Enter Your Weight: "))

bmi= weight / (hight ** 2)
print("Your BMI is : ",bmi)

if bmi<18.5:
    print("underweight")
elif bmi<=18.5 and bmi>=24.9:
    print("normal")
elif bmi<=25 and bmi>=29.9:
    print("overweight")
else:
    print("obese")