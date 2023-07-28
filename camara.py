import cv2
import tkinter as tk
from PIL import Image, ImageTk

def actualizar_camara():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img
    ventana.after(5, actualizar_camara)

ventana = tk.Tk()
ventana.title("Cámara bien WAZAAAA")

cap = cv2.VideoCapture(0)

label = tk.Label(ventana)
label.pack()

actualizar_camara()

ventana.mainloop()

cap.release()
cv2.destroyAllWindows()
