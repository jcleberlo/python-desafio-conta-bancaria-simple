menu = """
[D] Depositar
[S] Sacar
[E] Extrato

[Q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opção = input(menu).upper()
    if opção.upper() == "D":
        valor = float(input("Informe o valor a ser depositado: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado deve ser positivo!")
    elif opção == "S":
        valor = float(input("Informe o valor a ser sacado: R$ "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print(
                f"Operação falhou! Você não tem saldo suficiente! Saldo atual: R$ {saldo:.2f}"
            )
        elif excedeu_limite:
            print(
                f"Operação falhou! O valor excede o limite de saque de R$ {limite:.2f}!"
            )
        elif excedeu_saques:
            print(
                f"Operação falhou! Limite de {LIMITE_SAQUES} de saques diários foi excedido!"
            )
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado deve ser positivo!")
    elif opção == "E":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")
    elif opção == "Q":
        print("Saindo do programa...")
        break
    else:
        print("Operação inválida, por favor selecione novamente a opção:")
