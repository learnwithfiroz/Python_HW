x=float(input("Enter the X coordinat: "))
y=float(input("Enter the Y Coordinate: "))


if x>0 and y>0:
    print("Point is first Quadrant ")
elif x<0 and y>0:
    print("Point is second Quardant")
elif x<0 and y<0:
    print("Point is Third Quardant")
elif x<0 and y>0:
    print("Point is fourth Quardant")
else:
    print("Point Lies on axis")