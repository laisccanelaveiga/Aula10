
print("Caixa Eletrônico")

# cedulas_disponiveis = [200, 100, 50]

try:
    saldo = 1000
    print(f"Valor disponível: {saldo}")
    vlr_saque = float(input("Informe o valor para saque: "))

    if vlr_saque > saldo:
        print("Saldo insuficiente!")

    
    elif vlr_saque % 50 != 0:
        print("Notas disponíveis: [50][100][200]")


    elif 0 < vlr_saque <= saldo:
        print(f'Valor sacado: {vlr_saque}')
        saldo -= vlr_saque
        print(f'====Valor disponível: {saldo}')


except Exception as e:
    print(f'Erro Inesperado: {e}')    


except KeyboardInterrupt:
    print(f'Encerrado pelo Usuário.') 