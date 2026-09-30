n = int(input())
arr = list(map(int, input().split()))

expected = n * (n + 1) // 2
actual = sum(arr)

print(expected - actual)

# Time Complexity : O(n) -> We visit every element once.

# Space Complexity : Space = O(1) -> We only maintain two extra variables: expected and actual.