from operator import contains


class persona():

    def  _init_(self,nombre,telefono,documento):
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono
    def info(self):
        welcome = ("Bienvenido, {}")
        telefono = ("Telefono:  {}")
        documento = ("Documento:  {}")
        print(welcome.format(self.nombre))
        print(telefono.format(self.telefono))
        print(documento.format(self.documento))

persona1 = persona(input("Nombre de cliente: \t"),int(input("Telefono Cliente: \t")),int(input("Documento cliente: \t")))
vargorra = 1
varvesti = 2
varzapat = 3
varreloj = 4
varjean = 5
pregorra = 45000
prevesti = 75000 
prezapat = 120000
prereloj = 120000
prejean = 95000

def recibo(cantprod,prod):
    if prod == vargorra:
        if cantprod > 3:
            presindes = pregorra * cantprod
            preund = (pregorra * 0.85)
            pretot = preund * cantprod
            ahorro = presindes - pretot
            print("precio unidad: "+str(pregorra))
            print("precio unidad con descuento: "+str(preund))
            print("precio total: "+str(pretot))
            print("precio total sin descuento: "+str(presindes))
            print("ahorraste: "+str(ahorro))
        else:
            preund = pregorra
            pretot = pregorra * cantprod
            print("total: "+str(pretot))
    elif prod == varvesti:
        if cantprod > 3:
            presindes = prevesti * cantprod
            preund = (prevesti * 0.85)
            pretot = preund * cantprod
            ahorro = presindes - pretot
            print("precio unidad: "+str(prevesti))
            print("precio unidad con descuento: "+str(preund))
            print("precio total: "+str(pretot))
            print("precio total sin descuento: "+str(presindes))
            print("ahorraste: "+str(ahorro))
        else:
            preund = prevesti
            pretot = prevesti * cantprod
            print("total: "+str(pretot))
    elif prod == varzapat:
        if cantprod > 3:
            presindes = prezapat * cantprod
            preund = (prezapat * 0.85)
            pretot = preund * cantprod
            ahorro = presindes - pretot
            print("precio unidad: "+str(prezapat))
            print("precio unidad con descuento: "+str(preund))
            print("precio total: "+str(pretot))
            print("precio total sin descuento: "+str(presindes))
            print("ahorraste: "+str(ahorro))
        else:
            preund = prezapat
            pretot = prezapat * cantprod
            print("total: "+str(pretot))
    elif prod == varreloj:
        if cantprod > 3:
            presindes = prereloj * cantprod
            preund = (prereloj * 0.85)
            pretot = preund * cantprod
            ahorro = presindes - pretot
            print("precio unidad: "+str(prereloj))
            print("precio unidad con descuento: "+str(preund))
            print("precio total: "+str(pretot))
            print("precio total sin descuento: "+str(presindes))
            print("ahorraste: "+str(ahorro))
        else:
            preund = prereloj
            pretot = prereloj * cantprod
            print("total: "+str(pretot))
    elif prod == varjean:
        if cantprod > 3:
            presindes = prejean * cantprod
            preund = (prejean * 0.85)
            pretot = preund * cantprod
            ahorro = presindes - pretot
            print("precio unidad: "+ str(prejean))
            print("precio unidad con descuento: "+str(preund))
            print("precio total: "+str(pretot))
            print("precio total sin descuento: "+str(presindes))
            print("ahorraste: "+str(ahorro))
        else:
            preund = prejean
            pretot = prejean * cantprod
            print("total: "+str(pretot))
    else:
        print("variable incorrecta, vuelva a ingresar los datos")
        cantprod = 0
        prod = 0
lock = False
while lock == False:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nelije el producto a comprar \n"+"1. gorra: $45.000\n2. vestidos: $75.000 \n 3. zapatos: $120.000\n4. reloj: $120.000 \n5. jean: $95.000")
    print("\n\nproducto:  \n")
    ch1 = int(input())
    print("\n\ncantidad: ")
    ch2 = int(input())
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    persona1.info()
    print("\n")
    recibo(ch2,ch1)
    print("desea comprar otro producto? \t si: 1\tno: 0")
    lockb = int(input(""))
    if lockb == 1:
        lock = False
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    elif lockb == 0:
        lock = True
        print("Hasta luego!")
    else:
        print("valor invalido, vuelva a ingresar al sistema.")
        lock = True