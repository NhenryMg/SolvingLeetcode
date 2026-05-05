class Solution:
    def isValid(self, s: str) -> bool:
        # Paso 1: Crear un stack vacío (lista)
        stack = []
        
        # Paso 2: Crear diccionario que mapee cada cierre con su apertura correspondiente
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        # Paso 3: Recorrer cada carácter en el string s
        for char in s:
        
            # Paso 4: Si el carácter es de apertura ( (, [, { )
            if char in '([{':
            
                # Paso 4a: Agregar al stack
                stack.append(char)
                
            # Paso 5: Si el carácter es de cierre (), ], })
            else:
            
                # Paso 5a: Verificar si el stack está vacío
                if not stack:
                    # Si está vacío: return False (cierra sin haber abierto)
                    return False

                
                # Paso 5b: Verificar si el tope del stack coincide con la apertura esperada
                elif stack[-1] != pairs[char]:
                    # Usar el diccionario para saber qué apertura esperamos
                    # Si NO coincide: return Falso
                    return False
                
                
                # Paso 5c: Si SÍ coincide, hacer pop del stack (remover el paréntesis cerrado)
                else:
                    stack.pop()
        # Paso 6: Después de recorrer todo el string
        # Verificar si el stack está vacío
        if not stack:
            # Si vacío: return True (todos los paréntesis se cerraron correctamente)
            return True
        else:
            # Si NO vacío: return False (quedaron paréntesis sin cerrar)
            return False