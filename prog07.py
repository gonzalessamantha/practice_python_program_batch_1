# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
total = 0
for i in range(10):
    total += float(input(f"Enter number {i+1}: "))
print(total)