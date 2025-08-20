# WAP in Python to print odd integers in a given range

# Input range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Odd numbers between {start} and {end} are:")

# Using for loop
for i in range(start, end + 1):
    if i % 2 != 0:   # check odd
        print(i, end=" ")
