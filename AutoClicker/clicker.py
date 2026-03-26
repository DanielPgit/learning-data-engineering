import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# ================= CONFIGURACIÓN =================
TECLA_INICIO_PAUSA = KeyCode.from_char('s') 
TECLA_SALIR = KeyCode.from_char('e')

# CANTIDAD DE HILOS: 
# Con tu i5-14600KF, 8 hilos es el punto dulce para saturar Windows.
NUM_HILOS = 8 
# =================================================

mouse = Controller()
corriendo = False
programa_activo = True

def martillo_de_clics():
    """Función que ejecutan los hilos en paralelo"""
    global corriendo, programa_activo
    while programa_activo:
        if corriendo:
            # Bucle de fuerza bruta pura
            while corriendo:
                mouse.click(Button.left)
        time.sleep(0.1) # Respiro para la CPU en pausa

def al_presionar(key):
    global corriendo, programa_activo
    if key == TECLA_INICIO_PAUSA:
        corriendo = not corriendo
        estado = "🚀 MODO DIOS ACTIVADO" if corriendo else "⏸️ MOTOR DETENIDO"
        print(f"\n[STATUS] {estado}")
    elif key == TECLA_SALIR:
        corriendo = False
        programa_activo = False
        listener.stop()
        print("\n[INFO] Sistema apagado.")

# --- INICIO DEL MOTOR MULTI-HILO ---
print("="*50)
print(f"🔥 I5-14600KF EXTREME MULTI-THREAD ({NUM_HILOS} HILOS) 🔥")
print("="*50)
print(f" > [{TECLA_INICIO_PAUSA.char.upper()}] : ACTIVAR SOBRECARGA")
print(f" > [{TECLA_SALIR.char.upper()}] : ABORTAR")
print("-"*50)
print("ADVERTENCIA: Saturación masiva de Windows inminente.")

# Lanzamos los hilos
for i in range(NUM_HILOS):
    t = threading.Thread(target=martillo_de_clics, daemon=True)
    t.start()

with Listener(on_press=al_presionar) as listener:
    listener.join()
