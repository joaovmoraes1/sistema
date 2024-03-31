def depositar(saldo, valor):
    if valor > 0:
        saldo += valor
        return saldo, f"Depósito: R$ {valor:.2f}\n"
    else:
        return saldo, "Operação falhou! O valor informado é inválido."

def sacar(saldo, valor, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        return saldo, "Operação falhou! Você não tem saldo suficiente." 
    elif excedeu_limite:
        return saldo, "Operação falhou! O valor do saque excede o limite."
    elif excedeu_saques:
        return saldo, "Operação falhou! Número máximo de saques excedido."
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        return saldo, f"Saque: R$ {valor:.2f}\n"
    else:
        return saldo, "Operação falhou! O valor informado é inválido."

def gerar_extrato(extrato, saldo):
    return f"\n================ EXTRATO ================\n{extrato if extrato else 'Não foram realizadas movimentações.'}\n\nSaldo: R$ {saldo:.2f}\n=========================================="

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, msg = depositar(saldo, valor)
        print(msg)
        extrato += msg

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, msg = sacar(saldo, valor, limite, numero_saques, LIMITE_SAQUES)
        print(msg)
        if "Saque" in msg:
            extrato += msg

    elif opcao == "e":
        print(gerar_extrato(extrato, saldo))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
