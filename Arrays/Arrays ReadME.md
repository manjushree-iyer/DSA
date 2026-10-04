🧠 ARRAYS — LAST-MINUTE CHEAT SHEET

First ask these 5 questions
When you see ANY array problem, ask:

1. Do I need to scan every element?
        → Simple traversal

2. Do I need to compare from both ends?
        → Two pointers

3. Do I need to remember previous elements/counts?
        → Dictionary / Hash Map

4. Do I need a running sum/count/max/min?
        → Accumulator / Running variable

5. Does the question say CONTIGUOUS subarray?
        → Think Kadane / Prefix Sum / Sliding Window

🔎 COMMON ARRAY PATTERNS
Problem type	Think
Largest / Smallest: Running max/min
Second Largest:	largest + second
Sum / Average:	Accumulator
Count even/odd:	Counter
Reverse array:	Two pointers
Rotate array:	Save + Shift
Move zeros:	Placement pointer
Check sorted:	Compare adjacent elements
Remove duplicates from sorted array:	Compare adjacent
Frequency of elements:	Dictionary
Two Sum:	Hash Map
Leaders:	Traverse right → left + max_right
Maximum consecutive 1s:	current_streak + maximum_streak
Equilibrium index:	Total sum + left_sum
Merge sorted arrays:	Two pointers
Maximum subarray sum:	Kadane's Algorithm


🧩 THE BIG PATTERNS
🟢 1. Running Maximum / Minimum
When question says:
largest / smallest / maximum / minimum

Think:
maximum = arr[0]
for num in arr:    
if num > maximum:        
maximum = num


Pattern: Keep the best answer seen so far.
🟢 2. Accumulator
When question says:
sum / total / average

Think:
total = 0
for num in arr:   
total += num

Then:
average = total / n


Pattern: Keep adding to a running value.
🟢 3. Counter
When question says:
count how many...

Think:
count = 0
for num in arr:    
if condition:        
count += 1

Example:
if num % 2 == 0:    
even += 1


🔵 4. Two Pointers
When you need to work from both ends:
left = 0
right = n - 1
while left < right:    
# process    
left += 1    
right -= 1


Common problems:
Reverse Array
Two Sum (sorted version)
Palindrome
Some merging/partition problems

🔑 Remember:
Left + Right → move towards middle

🟣 5. Hash Map / Dictionary
When you need to:
remember something you've already seen

Think:
seen = {}


For frequency:
freq[num] = freq.get(num, 0) + 1


For Two Sum:
diff = target - arr[i]if diff in seen:    # found pairseen[arr[i]] = i


🔑 Remember:
"Have I seen this before?" → Dictionary

Usually:
O(n) time + O(n) space

🟠 6. Running Streak
When you see:
consecutive / continuous elements

Think:
current = 0
maximum = 0
for num in arr:    
if condition:        
current += 1        
maximum = max(maximum, current)    
else:        
current = 0


Example:
Maximum Consecutive Ones
1 1 0 1 1 1
      ↑
   reset

🔴 7. Kadane's Algorithm
When you see:
Maximum sum of a contiguous subarray

Immediately think:
current = arr[0]
maximum = arr[0]
for i in range(1, n):    
current = max(arr[i], current + arr[i])    
maximum = max(maximum, current)


🔑 The question you're asking:
"Start fresh or continue the previous subarray?"

Complexity:
O(n) time, O(1) space

🟡 8. Running Left/Right Information
Sometimes the question needs information about the elements before or after the current element.
Equilibrium Index
Think:
LEFT SUM | CURRENT | RIGHT SUM

Maintain:
total = sum(arr)left = 0

Then remove current from total to get right sum.
Leaders
When question says:
greater than all elements to its right

Think:
Go RIGHT → LEFT
Maintain:
max_right


Because you need to know the maximum element on the right.
🟤 9. Sorted Array = BIG CLUE
If the question says:
sorted array

STOP and notice it.
Sorted order gives you extra information.
Common opportunities:
Duplicates are adjacent
Two pointers can work
Binary Search may work
Merge can work

For example:
1 1 2 2 3 4 4
↑ ↑
duplicates together

⚡ COMPLEXITY CHEAT SHEET
What you're doing	Usually
One loop	O(n)
Two separate loops	O(n)
Nested loops	O(n²)
Dictionary lookup	O(1) average
Sorting	O(n log n)
Two pointers	O(n)
Extra array/dictionary of n elements	O(n) space
Only a few variables	O(1) space


VERY IMPORTANT:
O(n) + O(n) = O(n)

But:
O(n) × O(n) = O(n²)

Sequential loops → add
Nested loops → multiply