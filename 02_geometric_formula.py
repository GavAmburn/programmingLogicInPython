# Calculate the perimeter and area of the geometric elements: https://i.pinimg.com/736x/d5/e7/c1/d5e7c1535e1bd4136f3bac08b3304135.jpg

#git pull

#Circle
radius = int(input("Input your circle's radius"))
perimeter_circle = radius * 2 * 3.14
area_circle = 3.14 * radius ** 2

print ("Your perimeter is: ", perimeter_circle)
print ("Your area is: ", area_circle)
print("**********************************")


#Square
side = float(input("Digit the side of the square:"))
perimeter_square = side*4 
area_square = side*side
print("Square Perimeter: ", perimeter_square)
print("Square Area:", area_square)
print("**********************************")
#Triangle
side_a = float(input("Input side A of your Triangle:"))
side_b = float(input("Input side B of your Triangle:"))
side_c = float(input("Input side C of your Triangle:"))
height_tri = float(input("Input height of your Triangle:"))
perimeter_tri = side_a + side_b + side_c
area_tri = side_c * height_tri *.5

print("Your perimeter is: ", perimeter_tri)
print("Your area is: ", area_tri)

print("**********************************")
#Parallelogram
length_para = float(input("Input the length of your Parallelogram:"))
width_para = float(input("Input the width of your Parallelogram:"))
height_para = float(input("Input the height of your Parallelogram:"))
perimeter_para = 2 * (length_para + width_para)
area_para = length_para * width_para

print("Your perimeter is: ", perimeter_para)
print("Your area is: ", area_para)
print("**********************************")
#Rectangle
length_rect = float(input("Input the length of your Rectangle:"))
width_rect = float(input("Input the width of your Rectangle:"))
height_rect = float(input("Input the height of your Rectangle:"))
perimeter_rect = 2 * (length_rect + width_rect)
area_rect = length_rect * width_rect

print("Your perimeter is: ", perimeter_rect)
print("Your area is: ", area_rect)
print("**********************************")
#Rhombus
length_rhom = float(input("Input the length of your Rhombus:"))
width_rhom = float(input("Input the width of your Rhombus:"))
height_rhom = float(input("Input the height of your Rhombus:"))
perimeter_rhom = 2 * (length_rhom + width_rhom)
area_rhom = length_rhom * width_rhom

print("Your perimeter is: ", perimeter_rhom)
print("Your area is: ", area_rhom)

print("**********************************")
#Trapezoid
side_a_trap = float(input("Input side A of your Trapezoid:"))
side_b_trap = float(input("Input side B of your Trapezoid:"))
side_c_trap = float(input("Input side C of your Trapezoid:"))
side_d_trap = float(input("Input side D of your Trapezoid:"))
height_trap = float(input("Input height of your Trapezoid:"))
perimeter_trap = side_a_trap + side_b_trap + side_c_trap + side_d_trap
area_trap = ((side_a_trap + side_b_trap) / 2) * height_trap

print("Your perimeter is: ", perimeter_trap)
print("Your area is: ", area_trap)
print("**********************************")
#Regular n-agon
number_sides = float(input("Input the number of sides of your n-agon"))
length_sides = float(input("Input the length of one side of your n-agon"))
height_nagon = float(input("Input the height of your n-agon"))
perimeter_nagon = number_sides * length_sides
area_nagon = .5 * (height_nagon * length_sides * number_sides)

print("Your perimeter is: ", perimeter_nagon)
print("Your area is: ", area_nagon)
print("**********************************")
