
def excedente_pesca(pescado):
    kilo_exced = pescado - 100
    excedente = kilo_exced * 4
    return excedente, kilo_exced

try:
    pesc = float(input("Insira a quantidade pescada: "))


except (ValueError, TypeError):
        print("\nErro - Informe apenas números")
    
except KeyboardInterrupt:
        print("\nPrograma encerrado")

else:
    if pesc > 100:
        vlr_exc, kg_excedente = excedente_pesca(pesc)
        print(f'Total de kilos excedidos: {kg_excedente} kg \nValor excedente: R$ {vlr_exc:.2f}')
    else:
        print('Não há excedente')