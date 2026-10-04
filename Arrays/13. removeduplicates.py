n = int(input())
arr = list(map(int, input().split()))

result = [arr[0]]

for i in range(1, n):
    if arr[i] != arr[i - 1]:
        result.append(arr[i])

print(*result)

# Time Complexity : O(n) -> one for loop

# Space Complexity : O(n) -> we create a new variable result and the no. of elements stored can vary depeninding on the input.