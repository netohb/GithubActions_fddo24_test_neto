class Operaciones:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b


numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))


operacion = Operaciones(numero1, numero2)



print("ifjfinf feofi feioeff feife ijfe efijfoifeio efiefoief efifoief")
print(f"La suma de {numero1} y {numero2} es: {operacion.sumar()}")
print(f"La resta de {numero1} y {numero2} es: {operacion.restar()}")
