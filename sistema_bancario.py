menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        print("Qual valor você deseja depositar?")
        valor = float(input())
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print(f"Deposito de: R${valor:.2f}")
        print(f"Seu saldo é de: R${saldo:.2f}")
    elif opcao == "s":
        print("Saque")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excede_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida. Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação inválida. Excedeu o limite.")   

        elif excede_saques:
            print("Operação inválida. Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação inválida!")

    elif opcao == "e":
        print("Não foram realizadoas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")       

    elif opcao == "q":
       break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")