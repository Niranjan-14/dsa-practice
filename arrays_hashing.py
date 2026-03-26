
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
