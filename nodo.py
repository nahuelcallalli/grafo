class Nodo:
    
    def __init__(self, nombre):
        self.adyacentes=None
        self._nombre = nombre
       
    def agregarAdyacente(self,adyacente):
        if self.adyacentes==None:
            self.adyacentes=adyacente
            
        else:
            aux=self.adyacentes
            
            while aux.sig!=None:
                aux=aux.sig
                
            aux.agregar(adyacente)
            
    def emitir(self):
        aux=self.adyacentes
        print('{} ==> |'.format(self._nombre),end='')
        if aux!=None:
            aux.emitir()
            while aux.sig!=None:
                aux=aux.sig
                aux.emitir()
                
        print('|')