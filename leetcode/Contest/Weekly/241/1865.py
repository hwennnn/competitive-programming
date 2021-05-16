# 1865. Finding Pairs With a Certain Sum
# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

class FindSumPairs:
​
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.mp1 = collections.Counter(nums1)
        self.mp2 = collections.Counter(nums2)
​
    def add(self, index: int, val: int) -> None:
        num = self.nums2[index]
        self.mp2[num] -= 1
        self.nums2[index] += val
        self.mp2[num + val] += 1
​
    def count(self, tot: int) -> int:
        count = 0
        mp = collections.defaultdict(int)
        
        for k,v in self.mp1.items():
            if tot - k in self.mp2:
                count += v * self.mp2[tot - k]
        
        return count
​
​
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
