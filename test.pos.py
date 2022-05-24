from pynput import keyboard as kb
posmaxy = 100
posmaxx = 100
posminy = -100
posminx = -100
class character():
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
    
        
    def pulsa(self,tecla,posx,posy):
        if str(tecla) == 'Key.up':
            if (posy + 1) >= posmaxy:
                print("no puedes moverte mas hacia arriba!")
            else:
                posy = posy + 1
            print(posy)
        elif str(tecla) == 'Key.down':
            if (posy - 1) >= posminy:
                print("no puedes moverte mas hacia abajo!")
            else:
                posy = posy - 1
            print(posy)
        elif str(tecla) == 'Key.right':
            if (posx + 1) >= posmaxx:
                print("no puedes moverte mas hacia la derecha!")
            else:
                posx = posx + 1
            print(posx)
        elif str(tecla) == 'Key.left':
            if (posx - 1) >= posminx:
                print("no puedes moverte mas hacia la izquierda!")
            else:
                posx = posx - 1
            print(posx)
        else:
            print('Se ha pulsado la tecla ' + str(tecla))
        with kb.Listener(pulsa) as escuchador:
            escuchador.join()