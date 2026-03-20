# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
for i in range(100): # from 0-99
    if i % 10 != 0: # using modulus operator
        print(i)