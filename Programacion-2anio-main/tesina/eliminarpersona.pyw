import tkinter as tk

class Eliminart(tk.Tk):
    def __init__(self):
        super().__init__()

        self.usuario = "Silvana"
        self.contraseña = 1234
        self.geometry("400x200")  
        self.resizable(False, False)
        self.configure(bg="#40E0D0")  
        self.title("Eliminar persona")

        
        self.etiqueta1 = tk.Label(self, text="¿Desea eliminar a esta persona?", font=("Calibri", 20), bg=self.cget('bg'), fg="black")
        self.etiqueta1.grid(row=0, column=0, columnspan=2, pady=20)

        
        button_frame = tk.Frame(self, bg=self.cget('bg'))
        button_frame.grid(row=1, column=0, columnspan=2)

        
        button_si = tk.Button(button_frame, text="Si", font=("Calibri", 20), fg="green", width=10)
        button_no = tk.Button(button_frame, text="No", font=("Calibri", 20), fg="red", width=10)

        button_si.grid(row=0, column=0, padx=20, pady=10)
        button_no.grid(row=0, column=1, padx=20, pady=10)

EliminarP = Eliminart()
EliminarP.mainloop()
