s = input().lower()

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in freq:
    print(ch, ":", freq[ch])


# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(n) -> the length of the dictionary freq increases wrt the input size