"""
This program includes several functions for different tasks:
1. is_prime(num): Determines whether a given number is prime.
2. max_prime(): Reads integers from the user and returns the largest prime entered.
3. compression(s): Compresses a string by summarizing consecutive repeated characters.
4. sum_square(num): Returns the sum of the squares of the digits of a number.
5. is_happy(num): Determines if a number is "happy" using the sum_square function.
6. count_happy_numbers(): Counts how many happy numbers exist between 1 and 100.
All functions follow the constraints and logic described in the course assignment.
"""

def is_prime(num):
  if num < 2:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True
"""
Checks if a number is prime.
A number is considered prime if it's greater than 1 and has no divisors other than 1 and itself.
The loop goes only up to the square root of the number for efficiency.
"""

def max_prime():
    val = int(input("Enter a number: "))
    max_val = 1
    while val != -1:
        if is_prime(val):
            max_val = max(max_val, val)
        val = int(input("Enter a number: "))
    return max_val
"""
Reads a series of integers from the user until -1 is entered.
Returns the largest prime number entered using the is_prime function.
If no prime numbers were entered, returns 1 by default.
"""

def compression(s):
    counter = 1
    res = ""
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            counter += 1
        else:
            if counter > 1:
                res = res + s[i-1] + str(counter)
            else:
                res = res + s[i-1]
            counter = 1
    if len(s) > 0:
        if counter > 1:
            res += s[-1] + str(counter)
        else:
            res += s[-1]
    return res
"""
Compresses a string by encoding sequences of repeated characters.
A character repeated 2 or more times is written once, followed by its count.
Single characters are written as-is. The function also handles the last character correctly.
"""

def sum_square(num):
    num = str(num)
    total = 0
    for i in range(len(num)):
        total = total + int(num[i]) ** 2
    return total
"""
Compresses a string by encoding sequences of repeated characters.
A character repeated 2 or more times is written once, followed by its count.
Single characters are written as-is. The function also handles the last character correctly.
"""

def is_happy(num):
    counter = 0
    while num != 1:
        num = sum_square(num)
        counter += 1
        if counter > 10:
            return False
    return True
"""
Determines if a number is "happy".
A number is happy if repeatedly replacing it with the sum of the squares of its digits eventually leads to 1.
The process stops after 10 steps; if 1 hasn't been reached, the number is not happy.
"""

def count_happy_numbers():
    counter = 0
    for i in range(1, 101):
        if is_happy(i):
            counter += 1
    return counter
"""
Counts how many happy numbers exist in the range from 1 to 100 (inclusive).
Uses the is_happy function to check each number in the range.
"""
