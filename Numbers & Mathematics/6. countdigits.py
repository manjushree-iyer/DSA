n = input()
print(len(n))

# Time Complexity : O(log n) -> The number has d = O(log n) digits, and converting/reading those digits takes time proportional to d.
# Space Complexity : O(log n) ->  he string representation stores all d = O(log n) digits, so it uses space proportional to the number of digits.