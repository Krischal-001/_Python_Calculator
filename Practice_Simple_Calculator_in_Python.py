operation = input("Enter the operation you want to perform (+, -, *, /): ")
if operation not in ['+', '-', '*', '/']:
    print("Invalid operation selected.")
    exit()

n = int(input("Enter the number of values you want to perform the operation on: "))
numbers = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("You have entered:", numbers)

if operation == "+":
    result = sum(numbers)
    print("The sum is:", result)
elif operation == "-":
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    print("The difference is:", result)
elif operation == "*":
    result = 1
    for num in numbers:
        result *= num
    print("The product is:", result)
elif operation == "/":
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            print("Error: Division by zero is not allowed.")
            break
        result /= num
    else:
        print("The quotient is:", result)