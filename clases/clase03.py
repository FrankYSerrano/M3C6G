from .clase01 import Clase01
from .clase02 import Clase02

#CLASE
class Clase03 (Clase01, Clase02):
#ATRIBUTOS
    
#METODOS:
    def __init__ (self, arg1, arg2, arg3, arg4):
        self.atr1 = arg1
        self.atr2 = arg2
        self.atr3 = arg3
        self.atr4 = arg4
        Clase01.__init__(self, arg1, arg2, arg3, arg4)
        Clase02.__init__(self, arg1, arg2, arg3, arg4)
        print("Cree instancia de clase 03")

    def met1 (self, arg1):
        print("Clase 03 Metodo 1")

    def met2 (self, arg1):
        print("Clase 03 Metodo 2")

    def met3 (self, arg1):
        print("Clase 03 Metodo 3")
