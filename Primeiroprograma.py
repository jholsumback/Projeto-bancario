
menu = """

[d] DEPOSITAR
[s] SACAR
[e] EXTRATO
[q] SAIR

===> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
       
        valor = float(input("Qual valor deseja depositar? (Mínimo R$100,00)"))
       
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
           
      
    
    elif opcao == "s":
        valor = float(input("Qual valor deseja sacar?"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insulficiente")

        elif excedeu_limite:
            print("Operação falhou! Limite de saque diário é de no R$500,00")

        elif excedeu_saques:
            print("Operação falhou! Excedeu o limite de saques no dia")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")
    
        
       

    elif opcao == "e":
        print("\n=======================Ver extrato====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, digite a opção correta")





