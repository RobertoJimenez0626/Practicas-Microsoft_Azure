# Verificador de calificaciones
# Declaramos una variable
calificacion = input("Introduce tu calificación: ")
calificacion = int(calificacion)

# Preguntamos si la calificacion es menor a 700
if calificacion < 700 :
    print("Calificación reprobatoria") # Si es menor a 700, sale esto
elif calificacion == 700 :
    print("Calificación mínima aprobatoria")
elif calificacion > 1000 :
    print("No es posible sacar una calificación mayor a 1000")
else : # Si no se cumple el if anterior, pasa a esta linea
    print("Felicidades, tu calificacion es aprobatoria")
    # Se ejecuta si ninguno de los if se cumple

# Verificador de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("¡Bienvenido, puedes pasar!")
elif edad > 100 :
    print("No pueden ingresar personas de edad avanzada")
elif edad < 0 :
    print("No existen edades negativas")
else :
    print("No pueden entrar menores de edad")

# EN PYTHON NO HAY SWITCH CASE