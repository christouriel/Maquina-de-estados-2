#main.py
import tkinter as tk
from tkinter import ttk
from automata_pila import automata_pila_ab
from maquina_turing import ejecutar_maquina_turing
from automata_finito import validar_contrasena, Estado

class AutomataFinitoGUI:
    def __init__(self, master):
        self.master = master
        self.estado_actual = Estado.Q0

        self.label_estado = tk.Label(master, text="Escribe tu contraseña", font=("Helvetica", 16), foreground="#333")
        self.label_estado.pack(pady=20)

        self.entry_cadena = tk.Entry(master, width=20, font=("Helvetica", 12))
        self.entry_cadena.pack()

        self.boton_transicion = tk.Button(master, text="Revisar aceptación", command=self.realizar_transicion, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.boton_transicion.pack(pady=10)

    def realizar_transicion(self):
        entrada = self.entry_cadena.get()
        if entrada:
            resultado_validacion = validar_contrasena(entrada)
            if resultado_validacion == Estado.Q3:
                self.label_estado.config(text=f"Contraseña válida: {entrada}", fg="#4CAF50")
            else:
                self.label_estado.config(text="Cadena ingresada no es una contraseña válida", fg="#FF5733")

class AutomataPilaGUI:
    def __init__(self, master):
        self.master = master
        self.estado_actual = None

        self.label_estado = tk.Label(master, text="Escriba cadenas con la misma cantidad de 'a' y 'b'", font=("Helvetica", 16), foreground="#333")
        self.label_estado.pack(pady=20)

        self.entry_cadena = tk.Entry(master, width=20, font=("Helvetica", 12))
        self.entry_cadena.pack()

        self.boton_transicion = tk.Button(master, text="Revisar", command=self.realizar_transicion, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.boton_transicion.pack(pady=10)

    def realizar_transicion(self):
        entrada = self.entry_cadena.get()
        if entrada:
            resultado_transicion = automata_pila_ab(entrada)
            if resultado_transicion:
                self.label_estado.config(text="Cadena válida", fg="#4CAF50")
            else:
                self.label_estado.config(text="Cadena inválida", fg="#FF5733")

class MaquinaTuringGUI:
    def __init__(self, master):
        self.master = master
        self.label_estado = tk.Label(master, text="Inversa de binarios", font=("Helvetica", 16), foreground="#333")
        self.label_estado.pack(pady=20)

        self.entry_cadena = tk.Entry(master, width=20, font=("Helvetica", 12))
        self.entry_cadena.pack()

        self.boton_ejecutar = tk.Button(master, text="Ejecutar", command=self.ejecutar_maquina_turing, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.boton_ejecutar.pack(pady=10)

    def ejecutar_maquina_turing(self):
        entrada = self.entry_cadena.get()
        if entrada:
            resultado = ejecutar_maquina_turing(entrada)
            self.label_estado.config(text=resultado, fg="#4CAF50")

class AutomataGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz de Autómatas")

        # Definir un estilo para la interfaz
        style = ttk.Style()
        style.configure('TButton', foreground='white', background='#4CAF50')
        style.configure('TLabel', foreground='#333')
        style.configure('TFrame', background='#f0f0f0')

        self.tabControl = ttk.Notebook(master, style='TFrame')

        # Pestaña de Autómata Finito
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="Autómata Finito")
        self.automata_finito = AutomataFinitoGUI(self.tab1)

        # Pestaña de Autómata de Pila
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text="Autómata de Pila")
        self.automata_pila = AutomataPilaGUI(self.tab2)

        # Pestaña de Máquina de Turing
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text="Máquina de Turing")
        self.maquina_turing = MaquinaTuringGUI(self.tab3)

        self.tabControl.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomataGUI(root)
    root.mainloop()
