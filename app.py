#app.py

def area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser valores positivos y distintos de cero.")
    return (base * altura) / 2
