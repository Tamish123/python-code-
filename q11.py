rows = 5
# Top half
for i in range(rows):
    print("*" * (rows - i) + " " * (i * 2) + "*" * (rows - i))
# Bottom half
for i in range(rows):
    print("*" * (i + 1) + " " * ((rows - i - 1) * 2) + "*" * (i + 1))
