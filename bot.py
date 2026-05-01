import tkinter as tk
import random
from datetime import datetime

# respuestas del bot
respuestas = {
    "hola": ["Hola Gustavo 👋", "Hola 😄", "Que tal!"],
    "como estas": ["Estoy bien", "Funcionando correctamente", "Todo bien por aquí"],
    "linux": ["Linux es poderoso 🐧", "Zorin OS es muy bueno"],
    "python": ["Python es muy potente", "Python sirve para muchas cosas"]
}

def responder():
    mensaje = entrada.get().lower()
    chat.insert(tk.END, "Tú: " + mensaje + "\n")

    if mensaje in respuestas:
        respuesta = random.choice(respuestas[mensaje])
        chat.insert(tk.END, "Bot: " + respuesta + "\n")

    elif mensaje == "hora":
        chat.insert(tk.END, "Bot: " + datetime.now().strftime("%H:%M") + "\n")

    elif mensaje == "fecha":
        chat.insert(tk.END, "Bot: " + datetime.now().strftime("%d/%m/%Y") + "\n")

    elif mensaje == "salir":
        ventana.quit()

    else:
        chat.insert(tk.END, "Bot: No entendí eso 🤔\n")

    entrada.delete(0, tk.END)

# ventana
ventana = tk.Tk()
ventana.title("Chatbot de Gustavo")

# área de chat
chat = tk.Text(ventana, height=20, width=50)
chat.pack()

# entrada de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack()

# botón enviar
boton = tk.Button(ventana, text="Enviar", command=responder)
boton.pack()

ventana.mainloop()c