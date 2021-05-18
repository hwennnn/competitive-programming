# 609. Find Duplicate File in System
# https://leetcode.com/problems/find-duplicate-file-in-system

class Solution:
    def findDuplicate(self, paths):
        groups = collections.defaultdict(list)
        
        for path in paths:
            directory, *files = path.split()
            for file in files:
                name, content = file.split('(')
                groups[content].append(directory + '/' + name)
                
        return [g for g in groups.values() if len(g) > 1]
