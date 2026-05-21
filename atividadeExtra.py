dados = []

for dado in range(3):
    print("\nDados de vendas")
    dado = {
        "nome": input('Informe o nome do vendedor: '),
        "regiao": input('Informe a região do vendedor: '),
        "vlr_total": float(input('Informe o valor total vendido pelo vendedor: ')),
        "qnt_vendas": int(input("Informe a quantidade de produtos vendida: "))
    }
    
    if dado["vlr_total"] >= 5000:
        dados.append(dado)


print(dados)