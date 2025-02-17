#sistema bancário
#depósito / Saque e Extrato
#DEPÓSITOS: valores positivos, apenas 1 usuário, deposito em uma variável e na opção de extrato
#SAQUE: 3 saques diários e limite máximo de R$500 por saque, caso usuário não tenha saldo em conta, o sistema deve exibir uma msg informando que não será possível sacar. Todos os saques devem ser armazenados
#em uma variável e exibidos na operação extrato.
#EXTRATO: listar todos os saques e depósitos, no fim deve ser exibido o saldo atual da conta em R$.

#Método dos 5Qs:

#1- Quais são os dados de entrada necessários?
    #perguntar ao usuário qual opção ele deseja fazer, sacar, depositar ou ver extrato

#2- O que devo fazer com esses dados?
    #Se for depósito valores positivos, apenas 1 usuário, deposito em uma variável e na opção de extrato, se for SAQUE 3 saques diários e limite máximo de R$500 por saque, caso usuário não tenha saldo em conta, o sistema deve exibir uma msg informando que não será possível sacar. Todos os saques devem ser armazenados
#em uma variável e exibidos na operação extrato e se for EXTRATO: listar todos os saques e depósitos, no fim deve ser exibido o saldo atual da conta em R$.

#3- Quais as restrições do problema?
    #deve ter essas 3 opções para a conta do cliente

#4- Qual o resultado esperado?
    #resultado esperado é so cliente conseguir realizar saque, depósito e ver extrato

#5- Qual a sequencia de passos a ser feitos para chegar ao resultado esperado?
    #input ao usuário qual opção ele deseja realizar: saque, saldo ou extrato
    #[1]deposito >=100
    #   extrato
    #[2]Saque <= 500/dia 
        #saldo < saque exibir saldo insuficiente
    #[3]Extrato = saques, depositos
        #print saldo atual da conta

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
            print("Operação falhou! Limite de saque diário é de no máximo 3 vezes")

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





