s = input()

rev = ""

for ch in s:
    rev = ch + rev
print(rev)

# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(n) -> the length of variable rev increases wrt the input size