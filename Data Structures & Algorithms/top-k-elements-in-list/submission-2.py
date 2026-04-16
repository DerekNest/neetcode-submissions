
from collections import Counter
class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+ 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            result = []
        for i in range(len(buckets) -1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) ==k:
                    return result
   #could use heapq, which would be the following, it uses an extra log(k) for sorting the counts     
   # count = Counter(nums)
    #return heapq.nlargest(k, count.keys(), key=count.get)