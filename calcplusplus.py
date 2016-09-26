#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import sys
import calcoo
import calcoohija

if __name__ == "__main__":

    with open('fichero') as mifichero:
        lineas = csv.reader(mifichero)
        calculadora = calcoohija.CalculadoraHija()
        for linea in lineas:
            operacion = linea[0]
            linea.pop(0) 
            if operacion == "suma":
                result = int(0)
                for op in linea:
                    result = calculadora.plus(result, int(op))
                print(result)
            elif operacion == "resta":
                result = int(linea[0])
                linea.pop(0)
                for op in linea:
                    result = calculadora.minus(result, int(op))
                print(result)
            elif operacion == "multiplica":
                result = int(linea[0])
                linea.pop(0)
                for op in linea:
                    result = calculadora.multiply(result, int(op))
                print(result)
            elif operacion == "divide":
                result = int(linea[0])
                linea.pop(0)
                for op in linea:
                    try:
                        result = calculadora.div(result, int(op))
                    except ZeroDivisionError:
                        sys.exit("Division by zero is not allowed")
                print(result)
            else:
                print('Operación erronea.')
