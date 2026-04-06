# ====================================================================
# Date: 2 Apr 2026
# Problem: Valid Palindrome
# Pattern: Two Pointers
# Key insight: Clean string first (isalnum + lower)
#              Left pointer from start, right from end
#              Move inward while l < r
#              If mismatch → return False
# ====================================================================


def isPalindrome(self, s: str) -> bool:
    out = ""
    for i in s:
        if i.isalnum():
            out += i.lower()

    l = 0
    r = len(out) - 1
    while l < r:
        if out[l] != out[r]:
            return False
        l += 1
        r -= 1
    return True


# ================================================
# Date: 3 Apr 2026
# Problem: Two Sum II
# Pattern: Two Pointers on sorted array
# Key insight: Sorted array → move left pointer if sum too small
#              move right pointer if sum too big
#              Return 1-indexed result
# ================================================

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            l = 0
            r = len(numbers) - 1
            while l < r:
                total = numbers[l] + numbers[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    return [l+1, r+1]

# ================================================
# Date: 6 Apr 2026
# Problem: 3Sum
# Pattern: Two Pointers + sorting
# Solved alone? No — guided
# ================================================

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        num = sorted(nums)
        for i, j in enumerate(num):
            if i > 0 and num[i] == num[i-1]:
                continue
            left = i + 1
            right = len(num) - 1
            while left < right:
                val = num[i] + num[left] + num[right]
                if val == 0:
                    output.append([num[i], num[left], num[right]])
                    left = left + 1
                    right = right - 1
                    while left < right and num[left] == num[left - 1]:
                        left = left + 1
                    while right > left and num[right] == num[right + 1]:
                        right = right - 1
                if val < 0:
                    left = left + 1
                if val > 0:
                    right = right - 1
        return output