def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    if funcao == somar:
        print(f"O resultado da operação {a} + {b} = {resultado}")
    else:
        print(f"O resultado da operação {a} - {b} = {resultado}")

exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 4, subtrair)  # O resultado da operação 10 - 4 = 6