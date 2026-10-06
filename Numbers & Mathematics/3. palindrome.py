n = int(input())

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Palindrome" if original == reverse else "Not Palindrome")

# Time Complexity : O(d) -> Since the number itself has d digits.
# Space Complexity : O(1) -> no new data structure created