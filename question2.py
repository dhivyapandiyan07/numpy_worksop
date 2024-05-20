# find if the given number is a palindrome or not?
def is_palindrome(number):
    
    num_str = str(number)
    
    
    reversed_str = num_str[::-1]
    

    return num_str == reversed_str


number = 121  
if is_palindrome(number):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")