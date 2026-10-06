n = int(input())

reverse = 0

while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10

print(reverse)

# Time Complexity : O(log n) -> The loop runs once for every digit.
# Space Complexity : O(1) -> no new data structure created