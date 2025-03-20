from collections import Counter
from itertools import combinations

def solution(nums):
    n = len(nums)
    distinct_count = len(set(nums))
    
    return min(n//2, distinct_count)