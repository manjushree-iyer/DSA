s = input()

result = ""

for ch in s:
    if ch.isupper():
        result += ch.lower()
    else:
        result += ch.upper()

print(result)


# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(n) -> the length of the result variable increases wrt the input size