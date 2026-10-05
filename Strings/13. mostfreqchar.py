from collections import Counter

s = input()

freq = Counter(s)

maximum = max(freq.values())

for ch in s:
    if freq[ch] == maximum:
        print(ch)
        break

# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(n) -> because the frequency dictionary can contain up to n unique characters.