#criar um sistema bancario
#contendo as seguintes funções
#
#   Criar usuario:
#       usuarios = []
#       usuario = {"nome": ,"data nascimento" : ,
#                   "cpf" : , "endereço" : }
#           endereço = logradouro, nmr-bairro-cidade/sigla estado
#           cpf = cpf unico, somente numeros
#   Criar conta bancaria:
#       agencia (0001), numero da conta (sequencial), usuario(pode ter mais de uma conta - cpf)
#   depósito (saldo, valor, extrato) return saldo, extrato
#   Saque (*, saldo, valor, extrato, limite, numero_saques, limite_saques)
#   Extrato (saldo, \, extrato)

import textwrap

def menu():
    menu = """
        [nu]:\t\tNovo Usuário
        [nc]:\t\tNova Conta
        [lc]:\t\tListar Contas
        [d]:\t\tDepósito
        [s]:\t\tSaque
        [e]:\t\tExtrato
        [q]:\t\tSair
    """
    return input(textwrap.dedent(menu))

def criar_usuario(usuarios):

    cpf = input("Informe o CPF (Somente Numeros): ")
    usuario = verificar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe um usuário com este cpf! @@@")
        return 
    
    nome = input("Nome: ")
    data_de_nascimento = input(("Data de nascimento (dd-mm-aaaa): "))
    endereco = input("Endereço (logradouro, nmr-bairro-cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_de_nascimento":data_de_nascimento,"cpf":cpf,"endereço":endereco})
    print("Usuário criado com sucesso!")    
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF (SOMENTE NUMEROS): ")
    usuario = verificar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Conta criada com sucesso! @@@")
        return {"agência":agencia,"numero_da_conta":numero_conta,"usuario":usuario}
    
    print("\n@@@ ERROR! USUÁRIO NÃO ENCONTRADO! @@@")
    return

def verificar_usuario(cpf, usuarios):
    usuario_filtrado =  [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def deposito(saldo, valor, extrato):

    if valor <= 0:
        print("\n@@@ ERROR! VALOR INVÁLIDO! @@@")
        return
    
    saldo += valor
    extrato += f"Valor de depósito R$ {valor:.2f}"
    print("\n@@@ Depósito realizado com sucesso! @@@")

    return saldo, extrato

def saque(*, saldo, valor, limite, numero_saques, limite_saques, extrato):
    
    if numero_saques > limite_saques:
        print("\n@@@ ERROR! LIMITE DE SAQUES ATINGIDO! @@@")
    
    elif valor > limite:
        print("\n@@@ ERROR! VALOR DE LIMITE ULTRAPASSADO! @@@")
    
    elif valor > saldo:
        print("\n@@@ ERROR! SALDO INSUFICIENTE! @@@")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Valor de saque: R$ {valor:.2f}"
        numero_saques += 1
        print("@@@ Saque realizado! @@@")
    
    else:
        print("\n@@@ ERROR! VALOR INVÁLIDO! @@@")
    
    return saldo, extrato

def imprimir_extrato(saldo, /, extrato):

    print("\n@@@ EXTRATO! @@@")
    print("\n".join(extrato))
    print(f"\nSALDO: R$ {saldo:.2f}")

def imprimir_contas(contas):
    
    for conta in contas:
        linha = f"""\
            Agência:\t\t{conta["agência"]}
            C/C:\t\t{conta["numero_da_conta"]}
            Titular:\t\t{conta["usuario"]["nome"]}
        """

        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_da_conta = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_da_conta = len(contas) + 1
            conta_usuario = criar_conta(AGENCIA, numero_da_conta, usuarios)
            
            if conta_usuario:
                contas.append(conta_usuario)

        elif opcao == "lc":
            imprimir_contas(contas)
        
        elif opcao == "d":
            valor = float(input("Valor a ser depositado: R$ "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor de saque: R$ "))
            numero_saques += 1
            saldo, extrato = saque(saldo=saldo, valor=valor, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES, extrato=extrato)

        elif opcao == "e":
            imprimir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("@@@ ERROR! OPÇÃO INVÁLIDA! @@@")

main()