statement_one = False

statement_two = True

credits = 120
gpa = 1.8

if not credits >= 120:
    print("You do not have enough credits to graduate")
    
if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate")
    
if not credits >= 120 and not gpa >= 2.0:
    "You do not meet either requierements to graduate"
    
grade = 86

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
    
    # 1. Definimos el peso en la Tierra y el número del planeta
peso_tierra = 70  # Puedes cambiar este número
numero_planeta = 3 # Digamos que Codey va a Jupiter

# 2. Empezamos la "escalera" de decisiones
if numero_planeta == 1:
    peso_destino = peso_tierra * 0.91
    nombre_planeta = "Venus"
elif numero_planeta == 2:
    peso_destino = peso_tierra * 0.38
    nombre_planeta = "Mars"
elif numero_planeta == 3:
    peso_destino = peso_tierra * 2.34
    nombre_planeta = "Jupiter"
elif numero_planeta == 4:
    peso_destino = peso_tierra * 1.06
    nombre_planeta = "Saturn"
elif numero_planeta == 5:
    peso_destino = peso_tierra * 0.92
    nombre_planeta = "Uranus"
elif numero_planeta == 6:
    peso_destino = peso_tierra * 1.19
    nombre_planeta = "Neptune"
else:
    print("Ese número de planeta no existe en nuestra lista.")
    peso_destino = None

# 3. Mostramos el resultado si el planeta era válido
if peso_destino:
    print(f"Tu peso en {nombre_planeta} sería de {peso_destino} kg.")