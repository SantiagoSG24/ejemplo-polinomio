from datoPolinomio import datoPolinomio
from Polinomio import Polinomio
class Nodo:
    def __init__(self, info=None):
        self.info = info
        self.sig = None
    
    def agregar_termino(polinomio, termino, valor):
        """Agrega un termino y su valor al polinomio."""
    aux = Nodo()
    aux.info = datoPolinomio(termino, valor)
    if termino > polinomio.grado:
        aux.sig = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    else:
        actual = polinomio.termino_mayor
        while actual.sig is not None and termino < actual.sig.info.termino:
            actual = actual.sig
        aux.sig = actual.sig
        actual.sig = aux