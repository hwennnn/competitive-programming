# 2086. Minimum Number of Buckets Required to Collect Rainwater from Houses
# https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/

class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = list(street)
        n = len(street)
        
        for i, x in enumerate(street):
            if street[i] != "H": continue
            if i - 1 >= 0 and street[i - 1] == "B": continue
            
            if i + 1 < n and street[i + 1] == ".":
                street[i + 1] = "B"
            elif i - 1 >= 0 and street[i - 1] == ".":
                street[i - 1] = "B"
            else:
                return -1
        
        return street.count("B")
            
