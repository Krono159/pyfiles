
class persona():

    def  __init__(self,nombre,edad,cargo):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
    def info(self):
        infor = ("Hola! soy {}, tengo {} y soy {}")
        print(infor.format(self.nombre,self.edad,self.cargo))

persona1 = persona("ricardo",64,"Magister en desocupe")

persona1.info()
