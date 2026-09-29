n = int(input())
arr = list(map(int, input().split()))

total = 0

for num in arr:
    total += num

print(total)

# Time Complexity : O(n) -> We visit every element once.

# Space Complexity : Space = O(1) -> We only maintain one extra variable: total.