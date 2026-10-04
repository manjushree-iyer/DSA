n = int(input())
arr = list(map(int, input().split()))
target = int(input())

seen = {}

for i in range(n):
    diff = target - arr[i]

    if diff in seen:
        print(seen[diff], i)
        break

    seen[arr[i]] = i
else:
    print(-1)


# Time Complexity : O(n) -> we traverse the array only once

# Space Complexity : O(n) -> only one dictionary created which is seen whose size differs wrt the input size