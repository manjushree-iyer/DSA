n = int(input())
arr = list(map(int, input().split()))

count = 0
maximum = 0

for num in arr:
    if num == 1:
        count += 1
        maximum = max(maximum, count)
    else:
        count = 0

print(maximum)

# Time Complexity : O(n) -> we traverse the array only once

# Space Complexity : O(1) -> Only count and maximum are used.