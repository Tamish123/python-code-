

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and a < c:
    print("The minimum number is:", a)
elif b < a and b < c:
    print("The minimum number is:", b)
elif c < a and c < b:
    print("The minimum number is:", c)
else:
    print("Two or more numbers are equal and smallest.")
