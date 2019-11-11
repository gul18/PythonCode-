PI = 3.14
#surface area of cylinder
print("Input for cylinder\n")
r1 = float(input(" Enter the radius of a cylinder: "))
height = float(input(" Enter the height of a cylinder: "))
sa1 = 2 * PI * r1 * (r1 + height)
print("\n The surface area of a cylinder = %.2f" %sa1)

#surface area of sphere
r2 = float(input(" Enter the radius of a sphere: "))
sa2 =  4 * PI * r2 * r2
print("\n The surface area of a sphere = %.2f" %sa2)

#area of triangle
base = float(input(" Enter the base of the triangle:"))
height1 = float(input ("Enter the height of triangle:"))
area = 0.5 * height1 * base
print("\n The Area of Triangle is : %0.2f" %area)
print("End of code")

