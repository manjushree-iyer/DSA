n = int(input())

digits = str(n)
power = len(digits)

total = 0

for digit in digits:
    total += int(digit) ** power

print("Armstrong" if total == n else "Not Armstrong")

# Time Complexity : O(d) -> Since the number itself has d digits.
# Space Complexity : O(d) -> one variable created O(d) wherein 