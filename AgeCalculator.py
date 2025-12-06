age=float(input("Enter your Age: "))

if age>=0 and age<=1:
    print("Infant")
elif age>=2 and age<=3:
    print("Toddler")
elif age>=4 and age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
else:
    print("Adult")