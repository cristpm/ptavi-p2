#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):

	def multiply(op1,op2):
		return op1*op2

	def div(op1,op2):
		return op1/op2
		
if __name__ == "__main__":

    fich=open('fichero','r')
    lineas =fich.readlines()## guarda cada linea del fichero en una lista
    
    for linea in lineas:
        elementos = linea.split(',')## lista con cada caracter
        operacion = elementos[0]
        elementos.pop(0)##elimitamos la operacion de la lista
        if operacion == "suma":
            result = int(0)
            for op in elementos:
                result = CalculadoraHija.plus(result, int(op))
            print(result)
        elif operacion == "resta":
            result = int(elementos[0])
            elementos.pop(0)
            for op in elementos:
                result = CalculadoraHija.minus(result,int(op))
            print(result)
        elif operacion == "multiplica":
            result = int(elementos[0])
            elementos.pop(0)
            for op in elementos:
                result = CalculadoraHija.multiply(result,int(op))
            print(result)
        elif operacion == "divide":
            result = int(elementos[0])
            elementos.pop(0)
            for op in elementos:
                try:
                    result = CalculadoraHija.div(result,int(op))
                except ZeroDivisionError:
                    sys.exit("Division by zero is not allowed")
            print(result)
        else:
            print('Operación erronea.')
        
