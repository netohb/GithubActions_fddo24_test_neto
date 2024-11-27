def es_primo(numero):
    """Determina si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def es_par(numero):
    """Determina si un número es par."""
    return numero % 2 == 0
