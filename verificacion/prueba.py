class Operaciones:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def mult_bien (self):
        return self.a * self.b


numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))


operacion = Operaciones(numero1, numero2)

print(f"La suma de {numero1} y {numero2} es: {operacion.sumar()}")
print(f"La resta de {numero1} y {numero2} es: {operacion.restar()}")


print("Hola como están todos")

# Iniciar una variable para la suma
resultado = 0

# 4 bucles for anidados
for i in range(1):  # Primer bucle
    for j in range(1):  # Segundo bucle
        for k in range(1):  # Tercer bucle
            for contador in range(1):  # Cuarto bucle, cambiado 'l' por 'contador'
                # Sumar 2 y 2
                resultado = 2 + 2

# Imprimir el resultado
print("El resultado de la suma es:", resultado)

print("Hola")
