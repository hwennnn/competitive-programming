# 2115. Find All Possible Recipes from Given Supplies
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        R = set(recipes)
        supplies = set(supplies)
        n = len(recipes)
        mp = collections.defaultdict(set)
        res = set()
        
        for i, l in enumerate(ingredients):
            for ing in l:
                if ing in R:
                    mp[ing].add(i)
                    
        def go(l, i):
            if all(x in supplies for x in l):
                res.add(recipes[i])
                supplies.add(recipes[i])
                for child in mp[recipes[i]]:
                    go(ingredients[child], child)
                
        for i, l in enumerate(ingredients):
            go(l, i)
                   
        return list(res)
        
