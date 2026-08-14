#412. Fizz Buzz
# Given an integer n, return a string array answer (1-indexed) where:
    # answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    # answer[i] == "Fizz" if i is divisible by 3.
    # answer[i] == "Buzz" if i is divisible by 5.
    # answer[i] == i (as a string) if none of the above conditions are true.

class Solution:
    def fizzBuzz(self, n: int):
        ans = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans

# 1523. Count Odd Numbers in an Interval Range
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0

        for i in range(low, high + 1):
            if i % 2 != 0:
                count += 1

        return count

#OR

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2

        if low % 2 != 0 or high % 2 != 0:
            count += 1

        return count


# 1365. How Many Numbers Are Smaller Than the Current Number
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        answer = []

        for i in range(len(nums)):
            count = 0

            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1

            answer.append(count)

        return answer

#2520. Count the Digits That Divide a Number
# Given an integer num, return the number of digits in num that divide num.
# An integer val divides nums if nums % val == 0.

class Solution:
    def countDigits(self, num: int) -> int:
        original = num
        count = 0

        while num > 0:
            digit = num % 10

            if original % digit == 0:
                count += 1

            num = num // 10

        return count

# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

# 1281. Subtract the Product and Sum of Digits of an Integer
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0

        while n > 0:
            digit = n % 10

            product *= digit
            total += digit

            n //= 10

        return product - total

