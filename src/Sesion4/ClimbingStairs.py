class Solution:
    def climbStairs(self, n: int) -> int:
        
        # crear lista memo de tamaño n+1 llena de 0
        memo = [0] * (n + 1)
        
        def climb(i):
            
            # si i == 1 devolver 1
            if i == 1: return 1
            # si i == 2 devolver 2
            if i == 2: return 2            
            # si memo[i] != 0 devolver memo[i]
            if memo[i] != 0: return memo[i]

            
            # memo[i] = climb(i-1) + climb(i-2)
            memo[i] = climb(i-1) + climb(i-2)
            # devolver memo[i]
            return memo[i]
        
        # devolver climb(n)
        return climb(n)


print(Solution().climbStairs(9))