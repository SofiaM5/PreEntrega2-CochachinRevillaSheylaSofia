class Cliente():
    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
    
    def presentarse(self):
        print("Hola me llamo "+ self.nombre.title())

    def __str__(self):
        texto = "Nombre: {0}"
        return texto.format(self.nombre)
