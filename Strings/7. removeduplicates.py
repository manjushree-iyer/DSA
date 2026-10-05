s = input()

seen = set()
result = ""

for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch

print(result)

# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(n) -> the length of the set seen increases wrt the input size