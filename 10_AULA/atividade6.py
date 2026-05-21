def calc_imc(h,p):
    imc = p / (h * h)
    return imc


while True: 
    try:
        altura = float(input('Altura: '))
        peso = float(input('Peso: '))
        indice = calc_imc(altura,peso)
    

    except ValueError:
            print("\nErro - Informe apenas números")

    except ZeroDivisionError:
            print('Erro - Vendedor não pode ser zero - 0')
        
    except KeyboardInterrupt:
            print("\nPrograma encerrado")    
    
    else:      
        print(f"\nSeu imc é {indice:.2f}")
        
        match indice:

            case indice if indice > 40:
                print("Obesidade grau III")
            case indice if indice > 35:
                print("Obesidade grau II")
            case indice if indice > 30:
                print("Obesidade grau I")
            case indice if indice > 25:
                print("Acima do peso")
            case indice if indice > 18.5:
                print("Peso normal")
            case indice if indice > 17:
                print("Abaixo do peso")
            case _:
                print('Muito abaixo do peso')
        
        continuar = input("\nDeseja continuar [S/N]: ").strip().upper()
        if continuar != "S":
            break
    finally:
         print("Programa encerrado")