from robobopy.Robobo import Robobo
import time

# Configura la IP de conexión de Robobo
ROBOBO_IP = "192.168.1.112"

# Instancia de Robobo
rob = Robobo(ROBOBO_IP)

def presentacion():
    rob.sayText("¡Hola a todos! Soy Robobo y vengo con una misión importante: ¡vamos a resolver un laberinto y programar juntos!")
    time.sleep(2)
    rob.sayText("¿Quién quiere ser mi ayudante hoy?")

def saludar_alumno(nombre):
    rob.sayText(f"¡Encantado de conocerte, {nombre}! Hoy vas a ser mi ayudante de programación.")
    
def actividad_labyrinth():
    rob.sayText("Vale, equipo, esto es lo que vamos a hacer: tenemos un laberinto y vamos a ayudarme a atravesarlo transportando un objeto.")
    rob.sayText("Vosotros me vais a decir cómo moverme utilizando Scratch.")
    time.sleep(2)
    rob.sayText("¡Empezamos el laberinto! Dime qué bloques debería usar para avanzar.")

def reaccion_actividad(emocion):
    if emocion == "exito":
        rob.sayText("¡Claro que sí! ¡Vas por buen camino!")
    elif emocion == "duda":
        rob.sayText("Mmm... parece que se está complicando. ¿Y si pides a un amigo que te ayude?")
    elif emocion == "sin_respuesta":
        rob.sayText("No te preocupes, tómate tu tiempo.")

def despedida():
    rob.sayText("¡Chicos, lo habéis hecho genial! Hoy hemos aprendido a usar Scratch para programar y a resolver un laberinto. ¡Increíble trabajo en equipo!")
    rob.sayText("Gracias a todos por vuestra ayuda. ¡Nos vemos en la próxima aventura!")

def main():
    # Conexión inicial
    rob.connect()
    print("Iniciando actividad con Robobo...")

    # 1. Presentación y elección de ayudante
    presentacion()
    
    # Solicitar el nombre del ayudante manualmente
    nombre_ayudante = input("Por favor, ingresa tu nombre: ")
    if nombre_ayudante.strip() == "":
        nombre_ayudante = "amigo"  # Valor por defecto si no se ingresa un nombre
    saludar_alumno(nombre_ayudante)

    # 2. Explicación de la actividad del laberinto
    actividad_labyrinth()

    # 3. Simulación de reacciones en la actividad del laberinto con espera de Enter
    input("Presiona Enter para continuar con la siguiente reacción...")
    reaccion_actividad("exito")
    input("Presiona Enter para continuar con la siguiente reacción...")
    reaccion_actividad("duda")

    # 4. Despedida
    despedida()

    # Desconexión final
    rob.disconnect()
    print("Actividad finalizada con Robobo.")

# Ejecuta el main
if __name__ == "__main__":
    main()
