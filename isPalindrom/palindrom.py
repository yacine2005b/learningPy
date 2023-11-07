def is_palindrome_number(num):
    # Convert the number to a string
    stringNum = str(num)
    return stringNum == stringNum[::-1]


num = 12321
result = is_palindrome_number(num)

if result:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
