n = int(input())
arr = list(map(int, input().split()))

leaders = []

max_right = arr[-1]
leaders.append(max_right)

for i in range(n-2, -1, -1):
    if arr[i] >= max_right:
        max_right = arr[i]
        leaders.append(arr[i])

leaders.reverse()

print(*leaders)

# Time Complexity : O(n) -> we traverse the array only once

# Space Complexity : O(n) -> only one variable created Leaders whose size differs wrt the input size