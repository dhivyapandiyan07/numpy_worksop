#write a program to find the maximum of two numbers
def find_maximum(a, b):
    if a > b:
        return a
    else:
        return b
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
maximum = find_maximum(num1, num2)
print(f"The maximum of {num1} and {num2} is {maximum}.")