#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija
		
		
if __name__ == "__main__":

    fich=open('fichero','r')
    lineas =fich.readlines()## guarda cada linea del fichero en una lista
    fich.close()
    calculadora = calcoohija.CalculadoraHija()
    
    for linea in lineas:
        elementos = linea.split(',')## lista con cada caracter
        operacion = elementos[0]
        elementos.pop(0)##elimitamos la operacion de la lista
        if operacion == "suma":
            result = int(0)
            for op in elementos:
                result = calculadora.plus(result, int(op))
            print(result)
        elif operacion == "resta":
            result = int(elementos[0])
            elementos.pop(0)
            for op in elementos:
                result = calculadora.minus(result,int(op))
            print(result)
        elif operacion == "multiplica":
            result = int(elementos[0])
            elementos.pop(0)
            for op in elementos:
                result = calculadora.multiply(result,int(op))
            print(result)
        elif operacion == "divide":
            result = int(elementos[0])
            elementos.pop(0)
            for op in elementos:
                try:
                    result = calculadora.div(result,int(op))
                except ZeroDivisionError:
                    sys.exit("Division by zero is not allowed")
            print(result)
        else:
            print('Operación erronea.')
