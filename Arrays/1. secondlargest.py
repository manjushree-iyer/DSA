n = int(input())
arr = list(map(int, input().split()))

largest = float('-inf')
second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num

    elif largest > num > second:
        second = num

if second == float('-inf'):
    print(-1)
else:
    print(second)
    

# Time Complexity : O(n) -> because only one for loop
# Space Complexity : O(1) -> only a few variables are created like largest, second etc. No new data structures are created like another array etc that grows with n.