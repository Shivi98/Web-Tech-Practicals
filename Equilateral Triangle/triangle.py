def main():
    sides = input("Enter 3 sides of triangle (Like a b c): ").strip()
    sides = sides.split(" ")
    # sides = list(map(int, sides))
    sides = [int(i) for i in sides]
    if len(sides) == 3:
        print(triangleCheck(sides[0], sides[1], sides[2]))
    else:
        print("Invalid Input")
        print("Exiting")


def triangleCheck(side1, side2, side3):
    if side1 == side2 and side2 == side3 and side3 == side1:
        return "Equilateral Triangle"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isocles Triangle"
    else:
        return "Scalen Triangle"


main()
