"""
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution:
    #Metodo para verificar si el numero es palindrome y sera boleano ya que eso pide el problema
    def isPalindrome(self, number: int) -> bool:

        #Podemos convertir ese numero a texto para revertirlo
        text = str(number)

        #Invirtiendo la cadena de texto
        text_inverted = text[::-1]

        #Retornando si es palindromo o no
        return text == text_inverted
    

#Probando 

sol = Solution()

print(sol.isPalindrome(121))
print(sol.isPalindrome(909))
print(sol.isPalindrome(123))