"""
Docstring for SolvingLeetcode.src.Medium.RotateList

61. Rotate List
Medium

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


#INICIO DEL CODIGO
#Este es la estrutura de nuestra lista, una linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        # si la lista está vacía o tiene un solo nodo -> devolver head
        if not head or not head.next:
            return head
        
        # calcular longitud n y encontrar el último nodo
        current = head
        n = 1

        while current.next:
            current = current.next
            n += 1
        
        # k = k % n
        k = k % n #Calculamos el numero real de rotacion
        
        # si k == 0 -> devolver head
        if k == 0:
            return head #En caso de que sean rotaciones completas y exactas entonces la linkedlist queda igual por eso se devuelve el head
        
        # conectar el último nodo con head (hacer ciclo)
        current.next = head #Como al recorrer la lista current obtiene la tail, entonces unimos eso al head
        
        current = head
        
        # encontrar el nuevo tail (posición n - k - 1)
        steps = n - k - 1
        for _ in range(steps):
            current = current.next
        # el nuevo head será new_tail.next
        new_head = current.next
        
        # romper el ciclo
        current.next = None
        # devolver new_head
        return new_head