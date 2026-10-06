n = int(input())

total = 0

while n > 0:
    total += n % 10
    n //= 10

print(total)

# Time Complexity : O(log n) -> The loop runs once for every digit.
# Space Complexity : O(1) -> no new data structure created