class Nodo:
    def _init_(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def _init_(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(f"[{actual.codigo}: {actual.descripcion}]")
class Nodo:
    def _init_(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def _init_(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(f"[{actual.codigo}: {actual.descripcion}]")
            actual = actual.siguiente

    # Reto individual: Cuenta nodos
    def contar_nodos(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

class Pila:
    def _init_(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento;
        # controla el caso de pila vacía
        if len(self.items) == 0:
            print("La pila está vacía")
            return None
        return self.items.pop()

class Cola:
    def _init_(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento;
        # controla el caso de cola vacía
        if len(self.items) == 0:
            print("La cola está vacía")
            return None
        return self.items.pop(0)


# --- PRUEBAS CON LOS DATOS DE LA EVALUACIÓN ---
if __name__ == "__main__":
    print(" PRUEBA DE LISTA ENLAZADA ")
    lista = ListaEnlazada()
    lista.agregar("PF01","Variables")
    lista.agregar("PF02", "Condicionales")
    lista.agregar("PF03", "Bucles")
    lista.mostrar()
    print(f"Total de nodos: {lista.contar_nodos()}")

    print(" PRUEBA DE PILA (LIFO) ")
    pila = Pila()
    pila.apilar("PF01: Variables")
    pila.apilar("PF02: Condicionales")
    pila.apilar("PF03: Bucles")
    print("Sacando de la pila:", pila.desapilar())
    print("Sacando de la pila:", pila.desapilar())

    print(" PRUEBA DE COLA (FIFO) ")
    cola = Cola()
    cola.encolar("PF01: Variables")
    cola.encolar("PF02: Condicionales")
    cola.encolar("PF03: Bucles")
    print("Atendiendo de la cola:", cola.desencolar())
    print("Atendiendo de la cola:", cola.desencolar())