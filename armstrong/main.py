def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number


num1 = 153
if is_armstrong(num1):
    print(f"{num1} is an Armstrong number.")
else:
    print(f"{num1} is not an Armstrong number.")

num2 = 223
if is_armstrong(num2):
    print(f"{num2} is an Armstrong number.")
else:
    print(f"{num2} is not an Armstrong number.")
