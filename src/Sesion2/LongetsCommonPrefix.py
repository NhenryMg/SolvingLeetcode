"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""
"""
Este es uno de mis favoritos jsjsj
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Primero verificamos que la lista no este vacia
        if not strs:
            return "La lista esta vacia"
        
        # Ordenamos los strings y mas
        strs.sort()
        
        first, last = strs[0], strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return f' El prefijo mas largo es: {first[:i]}'
    

sol = Solution()

print(sol.longestCommonPrefix(["dog","racecar","car"]))
print(sol.longestCommonPrefix(["flight","flow","flower"]))