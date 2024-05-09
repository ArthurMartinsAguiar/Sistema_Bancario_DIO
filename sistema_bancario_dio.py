"sistema_bancario.py"
MENU = """
    [d] => deposito,
    [s] => saque,
    [e] => extrato,
    [q] => sair,
        
=> """
SAQUE_MAXIMO = 500
QNT_MAXIMA_SAQUES_DIARIOS = 3

#R$ xxxx.xx

#deposito, saque e extrato


saldo = 1000
qnt_saques = 0
extrato = """"""

while True:
    op = input(MENU)
   
    if op ==  "d":

        deposito = float(input("Valor do depósito: "))
        if deposito < 0:
            print("VALOR INVALIDO!")
            
        saldo += deposito
        extrato += f"Houve um depósito de R$ {deposito:.2f}."
    
    if op == "s":
        
        saque = float(input("Valor do saque: "))
        if saque <= saldo and saque <= SAQUE_MAXIMO and saque > 0:
            if qnt_saques >= 3:
                print("Limite máximo de saques diários")
            else:   
                saldo -= saque
                qnt_saques += 1
                print("Saque realizado")
                extrato += f"Houve um saque de R$ {saque:.2f}."
        
        elif saque > SAQUE_MAXIMO:
            print(f"VALOR DE SALDO EXCEDIDO! VALOR MÁXIMO : R$ {SAQUE_MAXIMO}")
        
        elif saque > saldo:
            print("Saque não realizado! Saldo insuficente!")
            print(f"Saldo: R$ {saldo:.2f}")
        
        else:
            print("VALOR INVALIDO!") 
        
    
    if op == "e":
        print("EXTRATO".center(10, "-"))
        for _ in extrato.split("."):
            print(_, end="\n")
        print(f"SALDO DISPONIVEL: R$ {saldo:.2f}")
        print("-"*17)
              
    if op == "q":
        break
