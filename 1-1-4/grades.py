grade = (int)(input("Please enter the grade you got on your last test:"))

if grade >= 90:
    print("You got an A")
elif grade <= 89 and grade >= 80:
    print("You got an B")
elif grade <= 79 and grade >= 70:
    print("You got an C")
elif grade < 69 and grade > 60:
    print("You got an D")
elif grade < 65:
    print("You got an F")

