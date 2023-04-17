#Area of the Geometric Shapes (3D and 2D)
import math
pg = input("Is the polygon, a two-dimensional polygon(2D) or a three dimensional polygon? \nEnter your choice: ")
if pg == '2d' or pg == '2D':
    side = int(input("How many number of sides?(0 & 3-8): "))
    if side == 0 or side == 'zero' or side == 'Zero' or side == 'ZERO':
        r = int(input("Enter the value of the radius of the circle: "))
        print ("Area of the Circle is", 3.14*r*r, "sq.units")
    elif side == 3 or side == 'Three' or side == 'three' or side == 'THREE':
        base = int(input("Enter the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        print("Area of the triangle is", 0.5*base*height, "sq.units")
    elif side == 4 or side == 'Four' or side == 'FOUR' or side == 'four':
        quad = int(input("1. Square \n2. Rectangle \n3. Parallelogram \n4. Trapezium \n5. Rhombus \nEnter Your Choice: "))
        if quad == 1 or quad == 'One' or quad == 'one' or quad == 'ONE':
            a = int(input("Enter the value of the side of the square: "))
            print ("Area of the square is", a*a, "sq.units")
        elif quad == 2 or quad == 'Two' or quad == 'TWO' or quad == 'two':
            l = int(input("Enter the value of the length of the rectangle: "))
            b = int(input("Enter the value of the breadth of the rectangle: "))
            print ("Area of the rectangle is", l*b, "sq.units")
        elif quad == 3 or quad == 'three' or quad == 'Three' or quad == 'THREE':
            b = int(input("Enter the value of the base of the parrallelogram: "))
            h = int(input("Enter the value of the height of the parrallelogram: "))
            print ("Area of the parallelogram is", b*h, "sq.units")
        elif quad == 4 or quad == 'four' or quad == 'Four' or quad == 'FOUR':
            a = int(input("Enter the value of one of the parallel sides of the trapezium: "))
            b = int(input("Enter the value of the other parallel side of the trapezium: "))
            h = int(input("Enter the value of the distance between the parallel sides of the trapezium: "))
            print ("Area of the trapezium is", 0.5*(a+b)*h, "sq.units")
        else:
            d1 = int(input("Enter the value of the first diagonal of the rhombus: "))
            d2 = int(input("Enter the value of the second diagonal of the rhombus: "))
            print ("Area of the rhombus is", 0.5*d1*d2, "sq.units")
    elif side == 5 or side == 'five' or side == 'Five' or side == 'FIVE':
        a = int(input("Enter the value of the apothem of the pentagon: "))
        s = int(input("Enter the value of the side of the pentagon: "))
        print ("Area of the pentagon is", 2.5*s*a,"sq.units")
    elif side == 6 or side == 'six' or side == 'Six' or side == 'SIX':
        t = int(input("Enter the value of the side of the hexagon: "))
        print ("Area of the hexagon is", 2.6*t*t, "sq.unit")
    elif side == 7 or side == 'seven' or side == 'SEVEN' or side == 'Seven':
        t = int(input("Enter the value of the side of the heptagon: "))
        print ("Area of the heptagon is", 3.634*t*t,"sq.units")
    elif side == 8 or side == 'eight' or side == 'Eight' or side == 'EIGHT':
        t = int(input("Enter the value of the side of the octagon: "))
        print ("Area of the Octagon is", 4.8*t*t, "sq.units")
else:
    it = int(input("1. Cube \n2. Cuboid \n3. Cone \n4. Cylinder \n5. Sphere \n6. Hemisphere \nEnter your choice: "))
    if it == 1 or it == 'One' or it == 'one' or it == 'ONE':
        a = int(input("Enter the value of the side of the cube: "))
        choice = input("LSA or TSA \nEnter your choice: ")
        if choice == 'lsa' or choice == 'LSA':
            print("Lateral Surface Area of the cube is", 4*a*a,"sq.units")
        else:
            print("Total Surface Area of the Cube is", 6*a*a,"sq.units")
    elif it == 2 or it == 'Two' or it == 'two' or it == 'TWO':
        h = int(input("Enter the value of the height of the cuboid: "))
        l = int(input("Enter the value of the length of the cuboid: "))
        b = int(input("Enter the value of the breadth of the cuboid: "))
        choice = input("LSA or TSA \nEnter your choice: ")
        if choice == 'lsa' or choice == 'LSA':
            print ("Lateral Surface Area of the Cuboid is", 2*h*(l+b), "sq.units")
        else:
            print ("Total Surface Area of the Cuboid is", 2*(l*b+b*h+l*h), "sq.units")
    elif it == 3 or it == 'Three' or it == 'three' or it == 'THREE':
        r = int(input("Enter the radius of the Cone: "))
        h = int(input("Enter the height of the Cone: "))
        l = int(input("Enter the slant height of the Cone: "))
        choice = input("LSA or TSA \nEnter your choice: ")
        if choice == 'lsa' or choice == 'LSA':
            print ("Lateral Surface Area of the Cone is", 3.14*r*l, "sq.units")
        else:
            print ("Total Surface Area of the Cone is", 3.14*r*(l+r), "sq.units")
    elif it == 4 or it == 'Four' or it == 'four' or it == 'FOUR':
        r = int(input("Enter the radius of the base of the cylinder: "))
        h = int(input("Enter the value of the height of the cylinder: "))
        choice = input("LSA or TSA \nEnter your choice: ")
        if choice == 'lsa' or choice == 'LSA':
            print ("Lateral Surface Area of the Cylinder is", 2*3.14*r*h, "sq.units")
        else:
            print("Total Surface Area of the Cylinder is", 2*3.14*r*(r+h), "sq.units")
    elif it == 5 or it == 'Five' or it == 'five' or it == 'FIVE':
        r = int(input("Enter the value of the radius of the sphere: "))
        print ("Surface Area of the Sphere is", 4*3.14*r*r, "sq.units")
    else:
        r = int(input("Enter the value of the radius of the hemisphere: "))
        choice = input("LSA or TSA \nEnter your choice: ")
        if choice == 'lsa' or choice == 'LSA':
            print ("Lateral Surface Area of the Hemisphere is", 2*3.14*r*r, "sq.units")
        else:
            print ("Total Surface Area of the Hemisphere is", 3*3.14*r*r, "sq.units")
