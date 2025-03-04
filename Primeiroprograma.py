import textwrap

def menu():
    menu = """\n
    ========================= MENU ========================
    [d]\tDEPOSITAR
    [s]\tSACAR
    [e]\tEXTRATO
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuario
    [q]\tSAIR
    ===> """
    return input(textwrap.dedent(menu))




def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Saldo insulficiente")
        
    elif excedeu_limite:
        print("Operação falhou! Limite de saque diário é de no máximo R$500,00")

    elif excedeu_saques:
        print("Operação falhou! Excedeu o limite de saques no dia")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n======================= EXTRATO ====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("========================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe seu endereço (logradouro, nr - bairro - cidade/sigla estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe numero do CPF do usuário")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado, criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES =3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    

    while True:

        opcao = menu()

        if opcao == "d":
       
            valor = float(input("Qual valor deseja depositar? (Mínimo R$100,00)"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input("Informe o valor do saque:)"))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,

            )
       
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

main()







