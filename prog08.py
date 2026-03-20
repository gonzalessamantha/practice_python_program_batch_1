# Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd_counter = 0
for i in range(10): # starting from 0-9
    while True:
        try:
            num = int(input(f"Enter number {i + 1}: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    if num % 2 != 0:
        odd_counter += 1
print(f"Total odd numbers: {odd_counter}")