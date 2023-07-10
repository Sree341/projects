def is_palindrome(input_given):
    new_string=str(input_given)
    reversed_string=new_string[::-1]
    if reversed_string==new_string:
        return("The given string is palindrome.")
    else:
        return("The given string is not palindrome.")
    
print(is_palindrome(input("Enter the string or number you want to check if palindrome: ")))
    