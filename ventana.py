import tkinter as tk
import random
import time
import datetime

for x in "as":
    controla = 0

def mostrar_gola():
    mensaje.config(text="HOLAAAAA")
    cambiar_color_fondo()
    controla = 0
    print(controla)
    return controla

def mostrar_tilin():
    mensaje.config(text="TILIN")
    cambiar_color_fondo()
    controla = 0
    print(controla)
    return controla

def mostrar_hora(controla):
    controla = 1

    print(controla)
    while controla == 1:
        print(controla)
        hora_actual = datetime.datetime.now()
        mensaje.config(text=hora_actual.strftime("%H:%M:%S"))
        cambiar_color_fondo()
        ventana.update()
        time.sleep(1)
    else:
        controla = 0
        print(controla)

def cambiar_color_fondo():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_hex = f"#{r:02x}{g:02x}{b:02x}"
    ventana.configure(bg=color_hex)

ventana = tk.Tk()
ventana.title("Ventana insana")
ventana.geometry("600x300")

mensaje = tk.Label(ventana, text="", font=("Arial", 70))
mensaje.pack(pady=20)

boton_mostrar = tk.Button(ventana, text="Mostrar HOLA", command=lambda: [mostrar_gola()])
boton_mostrar.pack()

boton_mostrar = tk.Button(ventana, text="Mostrar tilin", command=lambda: [mostrar_tilin()])
boton_mostrar.pack()

boton_mostrar = tk.Button(ventana, text="Mostrar Hora", command=lambda: [mostrar_hora(controla)])
boton_mostrar.pack()

ventana.mainloop()

print(controla)