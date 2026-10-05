s = input()

left = 0
right = len(s) - 1

flag = True

while left < right:
    if s[left] != s[right]:
        flag = False
        break

    left += 1
    right -= 1

print("YES" if flag else "NO")

# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(1) -> no new variables or data structures created