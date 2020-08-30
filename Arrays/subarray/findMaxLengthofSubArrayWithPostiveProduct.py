# find Maximum Length of Subarray With Positive Product
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
arr = [1,-2,-3,4]
lastZero = -1
firstNegative = -1
numberofNegatives = 0
res = 0

for i,x in enumerate(arr):
    if x < 0:
        numberofNegatives += 1
        if firstNegative == -1:
            firstNegative = i
            
    if x == 0:
        numberofNegatives = 0
        firstNegative = -1
        lastZero = i
    else:
        if numberofNegatives % 2 == 0:
            res = max(res, i-lastZero)
        else:
            res = max(res, i - firstNegative)

print(res)


