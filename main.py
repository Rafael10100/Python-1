saldo = 0
extrato = ""
limite_saques = 3
numero_saques = 0

while True:
    opcao = input("Selecione uma opção:\n"
                  "1 - Depósito\n"
                  "2 - Saque\n"
                  "3 - Extrato\n"
                  "4 - Sair\n"
                  "Opção: ")

    if opcao == "1":
        valor_deposito = float(input("Informe o valor do depósito: "))
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print("Depósito realizado com sucesso!")

    elif opcao == "2":
        if numero_saques < limite_saques:
            valor_saque = float(input("Informe o valor do saque: "))
            if valor_saque <= 500 and valor_saque <= saldo:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")
            else:
                print("Saque não permitido.")
        else:
            print("Limite de disponível diários atingido.")

    elif opcao == "3":
        print("\n=== Extrato ===")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")

    elif opcao == "4":
        print("Obrigado por utilizar o sistema bancário!")
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")