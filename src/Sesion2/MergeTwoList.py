from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Crear nodo dummy
        dummy = ListNode()

        # 2. Crear puntero current que apunte a dummy
        current = dummy

        # 3. Ciclo while mientras ambas listas tengan nodos
        while list1 and list2:

            # 4. Comparar valores y elegir el menor
            if list1.val < list2.val:

                # 5. Conectar current.next al nodo elegido
                current.next = list1

                # 6. Avanzar en la lista elegida
                list1 = list1.next

                # 7. Avanzar current
                current = current.next

            else:
                current.next = list2
                list2 = list2.next
                current = current.next

        
        # 8. Después del ciclo, conectar los nodos restantes
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        # 9. Devolver dummy.next
        return dummy.next
    
# 10. Probando el codigo y funciones auxiliares
# Para imprimir el resultado, necesitas recorrer la lista
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Primero crea las listas enlazadas manualmente
# Lista 1: 1 → 2 → 3
n3 = ListNode(3)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

# Lista 2: 4 → 5 → 6
n6 = ListNode(6)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)

sol = Solution()

result = sol.mergeTwoLists(n1, n4)

print_linked_list(result)