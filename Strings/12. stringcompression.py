s = input()

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)

# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(n) -> result can grow with the size of the input