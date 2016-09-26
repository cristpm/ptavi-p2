#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def multiply(self, op1, op2):
        return op1*op2

    def div(self, op1, op2):
        return op1/op2

if __name__ == "__main__":
    calculadora = CalculadoraHija()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calculadora.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadora.minus(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = calculadora.multiply(operando1, operando2)
    elif sys.argv[2] == "divide":
        try:
            result = calculadora.div(operando1, operando2)
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")

    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
