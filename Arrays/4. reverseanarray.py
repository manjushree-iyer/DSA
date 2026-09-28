n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(*arr)

# Time Complexity : O(n) -> only one while loop
# Space Complexity : O(1) ->  no extra data structures created 