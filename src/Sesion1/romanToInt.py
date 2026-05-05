"""
Docstring for SolvingLeetcode.src.Sesion1.romanToInt

Este es basicamente recibir un input de tipo de texto en numero romanos y que el programa nos lo regrese en modo entero
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        #Creamos nuestro "diccionario mágico" de valores
        valores = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        #Inicializamos nuestro contador en CERO
        total = 0
        n = len(s)  # Cuántas letras tiene el número romano
        
        #Recorremos cada letra del número romano
        for i in range(n):
            #Preguntamos: ¿La letra actual es MENOR que la siguiente?
            if i < n - 1 and valores[s[i]] < valores[s[i + 1]]:
                #Si SÍ es menor → RESTAMOS
                total -= valores[s[i]]
            else:
                #Si NO es menor → SUMAMOS normalmente
                total += valores[s[i]]
        
        #Devolvemos el resultado final
        return total
    

#pruebas
sol = Solution()
print(sol.romanToInt("III")) #Devuelve 3
print(sol.romanToInt("VI")) #Devuelve 6
print(sol.romanToInt("XXXXIX")) #Devuelve 9