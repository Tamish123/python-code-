# Program to check if a number is divisible by 3 and ends with digit 4

num = int(input("Enter a number: "))

if (num % 3 == 0 and num % 10 == 4):
    print("The number is divisible by 3 and its last digit is 4.")
else:
    print("he number is  not divisible by 3 and its last digit is 4")
