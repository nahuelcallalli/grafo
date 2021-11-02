class Adyacente:
    sig=None
    
    def __init__(self, nombre, peso):
        self._peso = peso
        self._nombre = nombre


    def agregar(self,adyacente):
        self.sig=adyacente
    def emitir(self):
        print('[ {} -> {} ]'.format(self._nombre,self._peso),end='')