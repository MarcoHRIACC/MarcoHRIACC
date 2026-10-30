import turtle
import time
import random
import os

# Configuración inicial de la pantalla
pantalla = turtle.Screen()
pantalla.title("Super Car Race - Autos Reales")
pantalla.bgcolor("#2e2e2e")
pantalla.setup(width=800, height=600)
pantalla.tracer(0)

# Variables globales
puntos_vuelta = 0
tiempo_inicio = time.time()
juego_activo = True
tiempo_final = time.time()
obstaculos = []
colores_obstaculos = ["#e74c3c", "#e67e22", "#f1c40f", "#9b59b6"]

# --- 🛠️ DISEÑO DE AUTO REAL MEDIANTE COORDENADAS ---
# Definimos los puntos (X, Y) para dibujar un auto con ruedas y parabrisas
diseño_auto = (
    (-10, -20), (-12, -20), (-12, -15), (-10, -15),  # Rueda trasera izquierda
    (-10, -5),  (-12, -5),  (-12, 0),   (-10, 0),    # Rueda delantera izquierda
    (-10, 20),  (10, 20),                             # Parachoques delantero
    (10, 0),    (12, 0),    (12, -5),   (10, -5),    # Rueda delantera derecha
    (10, -15),  (12, -15),  (12, -20),  (10, -20),   # Rueda trasera derecha
    (10, -25),  (-10, -25)                            # Parachoques trasero
)

# Registramos el nuevo diseño en el sistema de Turtle
pantalla.register_shape("auto_real", diseño_auto)

# --- CREAR AL JUGADOR ---
jugador = turtle.Turtle()
jugador.speed(0)
jugador.shape("auto_real")
jugador.color("#3498db")  # Tu auto será Azul Deportivo
jugador.penup()
jugador.goto(0, -200)
jugador.setheading(90)  # Mirando hacia arriba

# Marcador y Cartel
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(-380, 260)

cartel = turtle.Turtle()
cartel.speed(0)
cartel.color("red")
cartel.penup()
cartel.hideturtle()

# Línea de meta
meta = turtle.Turtle()
meta.speed(0)
meta.color("white")
meta.penup()
meta.goto(-400, 220)
meta.pendown()
meta.pensize(4)
for _ in range(20):
    meta.forward(25)
    meta.penup()
    meta.forward(25)
    meta.pendown()
meta.hideturtle()

def reproducir_sonido_choque():
    if os.name == 'nt':
        import winsound
        try:
            winsound.Beep(500, 100)
            winsound.Beep(300, 200)
        except:
            pass
    else:
        os.system('echo -e "\\a"')

def actualizar_marcador():
    marcador.clear()
    tiempo_actual = int(time.time() - tiempo_inicio) if juego_activo else int(tiempo_final - tiempo_inicio)
    marcador.write(f"Vueltas: {puntos_vuelta}  |  Tiempo: {tiempo_actual}s", font=("Arial", 16, "bold"))

# Movroles
velocidad_jugador = 25

def mover_izquierda():
    if juego_activo and jugador.xcor() > -370:
        jugador.setx(jugador.xcor() - velocidad_jugador)

def mover_derecha():
    if juego_activo and jugador.xcor() < 370:
        jugador.setx(jugador.xcor() + velocidad_jugador)

def mover_arriba():
    if juego_activo and jugador.ycor() < 280:
        jugador.sety(jugador.ycor() + velocidad_jugador)

def mover_abajo():
    if juego_activo and jugador.ycor() > -280:
        jugador.sety(jugador.ycor() - velocidad_jugador)

def reiniciar_juego():
    global puntos_vuelta, tiempo_inicio, juego_activo, obstaculos
    if not juego_activo:  
        cartel.clear()
        puntos_vuelta = 0
        tiempo_inicio = time.time()
        
        jugador.goto(0, -200)
        
        for obs in obstaculos:
            obs.hideturtle()
        obstaculos.clear()
        
        crear_obstaculos()
        juego_activo = True
        bucle_principal()

# Configurar Teclado
pantalla.listen()
pantalla.onkeypress(mover_izquierda, "Left")
pantalla.onkeypress(mover_derecha, "Right")
pantalla.onkeypress(mover_arriba, "Up")
pantalla.onkeypress(mover_abajo, "Down")
pantalla.onkeypress(reiniciar_juego, "space")  

def crear_obstaculos():
    for _ in range(5):
        obs = turtle.Turtle()
        obs.speed(0)
        obs.shape("auto_real")  # ¡Ahora los obstáculos también tienen forma de auto!
        obs.color(random.choice(colores_obstaculos))
        obs.penup()
        obs.goto(random.randint(-350, 350), random.randint(0, 250))
        obs.setheading(270)  # Mirando hacia abajo (vienen en contra de ti)
        obstaculos.append(obs)

# Inicializar tráfico
crear_obstaculos()

# Bucle dinámico
def bucle_principal():
    global juego_activo, puntos_vuelta, tiempo_final
    
    if juego_activo:
        pantalla.update()
        actualizar_marcador()

        for obs in obstaculos:
            # Los rivales bajan por la pista
            obs.sety(obs.ycor() - random.randint(4, 9))
            
            if obs.ycor() < -300:
                obs.goto(random.randint(-350, 350), random.randint(250, 290))
                obs.color(random.choice(colores_obstaculos))

            # Ajuste de colisión por la nueva forma geométrica
            if jugador.distance(obs) < 30:
                juego_activo = False
                tiempo_final = time.time()
                actualizar_marcador()
                
                cartel.goto(0, 30)
                cartel.color("red")
                cartel.write("¡CHOQUE DE AUTOS! 💥", align="center", font=("Arial", 24, "bold"))
                cartel.goto(0, -20)
                cartel.color("white")
                cartel.write("Presiona [ESPACIO] para reiniciar la carrera", align="center", font=("Arial", 14, "normal"))
                pantalla.update()
                
                reproducir_sonido_choque()
                return 

        if jugador.ycor() >= 220:
            puntos_vuelta += 1
            jugador.sety(-260)

        pantalla.ontimer(bucle_principal, 20)

bucle_principal()
pantalla.mainloop()
