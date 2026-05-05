"""
1. Suma de dos
Dada una matriz de enteros y un entero , devuelve índices de los dos números de tal manera que se suman al objetivo.numstarget
Puede suponer que cada entrada tendría exactamente una solución y no puede usar el mismo elemento dos veces.
Puede devolver la respuesta en cualquier orden.

Ejemplo 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Ejemplo 2:

Restricciones:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Solo existe una respuesta válida.
"""


#Libreria para usar correctamente las listas
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Diccionario para almacenar número -> índice
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Verificar si el complemento ya está en el mapa
            if complement in num_map:
                return [num_map[complement], i]
            
            # Guardar el número actual con su índice
            num_map[num] = i
        
        return []  # En teoría nunca llega aquí por las restricciones
    
#Probando el codigo

sol = Solution()

print(sol.twoSum([7,2,3], target=9))
print(sol.twoSum([3,2,4], target=6))