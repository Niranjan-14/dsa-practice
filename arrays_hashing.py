
# ===============================
# Date: 25 Mar 2026
# Problem: Two Sum
# Pattern: HashMap
# ===============================

n = [2,7,11,5]
target = 9

def two_sum(n):
	notepad = {}
	for i, num in enumerate(n):
		complement = target - num

		if complement in notepad:
			return (notepad[complement], i)
		notepad[num]=i

# ===================================================
# Date: 25 Mar 2026
# Problem: Valid Anagram
# Pattern: HashMap — count up for s, count down for t
# ===================================================

def anagram(s,t):
     if len(s) != len(t):
          return False

     count = {}

     for val in s:
          if val in count:
               count[val] = count[val] + 1
          else:
               count[val] = 0

     for val in t:
          if val in count:
               count[val] = count[val] - 1
          else:
               count[val] = -1

     for val in count.values():
          if val != 0:
               return False

     return True

# ===============================
# Date: 25 Mar 2026
# Problem: Contains Duplicate
# Pattern: Set
# ===============================

def duplicates(l):
	s = set(l)

	if len(s) == len(l):
		return False
	return True


# ===============================
# Date: 26 Mar 2026
# Problem: Group Anagrams
# Pattern: HashMap with sorted string as key
# ===============================

def groupAnagrams(words):
    groups = {}
    
    for word in words:
        key = "".join(sorted(word))     
        
        if key in groups:
            groups[key].append(word)      
        else:
            groups[key] = [word] 
    
    return list(groups.values())  


# ===============================
# Date: 26 Mar 2026
# Problem: Top K Frequent Elements
# Pattern: HashMap + Sort
# ===============================

def topKFrequent(nums, k):
    counts = {}
    
    for num in nums:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1
    
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    for i in range(k):
        result.append(sorted_counts[i][0])
    
    return result

# ===============================
# Date: 27 Mar 2026 
# Problem: Product of Array Except Self 
# Pattern: Prefix + Suffix products
# ===============================


def productExceptSelf(nums):
    n = len(nums)
    
    # Build prefix
    prefix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]
    
    # Build suffix
    suffix = [1] * n
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]
    
    # Build output
    result = []
    for i in range(n):
        result.append(prefix[i] * suffix[i])
    
    return result


# ===============================
# Date: 30 Mar 2026 
# Problem: Valid Sudoku 
# Pattern: 3 lists of 9 sets (rows, cols, boxes)
# ===============================

def isValidSudoku(self, board):
    rows = [set() for i in range(9)]
    cols = [set() for i in range(9)]
    boxes = [set() for i in range(9)]
    
    for row in range(9):
        for col in range(9):
            val = board[row][col]
            if val == ".":
                continue
            box_number = (row // 3) * 3 + (col // 3)
            if val in rows[row]:
                return False
            else:
                rows[row].add(val)
            if val in cols[col]:
                return False
            else:
                cols[col].add(val)
            if val in boxes[box_number]:
                return False
            else:
                boxes[box_number].add(val)
    return True

# ==========================================================
# Date: 31 Mar 2026
# Problem: Encode/Decode Strings
# Pattern: Length prefix encoding
# Key insight: {length}#{string} — decoder reads 
#              length first, then exactly that many chars
#              No delimiter needed — length guides the read
# =========================================================

class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        for word in strs:
            encode_string += str(len(word)) + "#" + word
        return encode_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            i = j + 1 + length
            result.append(word)
        return result