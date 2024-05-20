#write a program to find the sum of digits of a given number'
def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum

num = int(input("Enter a number: "))
if num < 0:
    print("Please enter a non-negative number.")
else:
    result = sum_of_digits(num)
    print(f"The sum of the digits of {num} is {result}.")