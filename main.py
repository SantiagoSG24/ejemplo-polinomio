from datoPolinomio import datoPolinomio
from Nodo import Nodo   
from Polinomio import Polinomio

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

def modificar_termino(polinomio, termino, valor):
    """Modifica un termino del polinomio."""
    aux = polinomio.termino_mayor
    while aux is not None and aux.info.termino != termino:
        aux = aux.sig
    if aux is not None:
        aux.info.valor = valor

def obtener_valor(polinomio, termino):
    """Devuelve el valor de un termino del polinomio."""
    aux = polinomio.termino_mayor
    while aux is not None and aux.info.termino > termino:
        aux = aux.sig
    if aux is not None and aux.info.termino == termino:
        return aux.info.valor
    else:
        return 0
    

    def mostrar_polinomio(polinomio):
        """Muestra el polinomio en forma legible."""
        aux = polinomio.termino_mayor
        resultado = []
        while aux is not None:
            termino = f"{aux.info.valor}x^{aux.info.termino}" if aux.info.termino != 0 else f"{aux.info.valor}"
            resultado.append(termino)
            aux = aux.sig
        print(" + ".join(resultado))


        def sumar_polinomios(polinomio1, polinomio2):
            """Suma dos polinomios y devuelve el resultado."""
            resultado = Polinomio()
            aux1 = polinomio1.termino_mayor
            aux2 = polinomio2.termino_mayor

            while aux1 is not None or aux2 is not None:
                if aux1 is not None and (aux2 is None or aux1.info.termino > aux2.info.termino):
                    agregar_termino(resultado, aux1.info.termino, aux1.info.valor)
                    aux1 = aux1.sig
                elif aux2 is not None and (aux1 is None or aux2.info.termino > aux1.info.termino):
                    agregar_termino(resultado, aux2.info.termino, aux2.info.valor)
                    aux2 = aux2.sig
                else:
                    suma_valores = aux1.info.valor + aux2.info.valor
                    if suma_valores != 0:
                        agregar_termino(resultado, aux1.info.termino, suma_valores)
                    aux1 = aux1.sig
                    aux2 = aux2.sig

            return resultado
        


        def multiplicar_polinomios(polinomio1, polinomio2):
            """Multiplica dos polinomios y devuelve el resultado."""
            resultado = Polinomio()
            aux1 = polinomio1.termino_mayor

            while aux1 is not None:
                aux2 = polinomio2.termino_mayor
                while aux2 is not None:
                    termino = aux1.info.termino + aux2.info.termino
                    valor = aux1.info.valor * aux2.info.valor
                    valor_existente = obtener_valor(resultado, termino)
                    modificar_termino(resultado, termino, valor_existente + valor)
                    aux2 = aux2.sig
                aux1 = aux1.sig

            return resultado
        
        