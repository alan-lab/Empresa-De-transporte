LIMITE_MAXIMO = 50  
linhas = []  
linhas_sobrecarregadas = 0 
def cadastrar_linha():
    """
    Solicita os dados de uma nova linha de ônibus, verifica se está
    sobrecarregada e retorna um dicionário (registro) com os dados.
    """
    while True:
        try:
            numero = input("Digite o número da linha: ")
            if not numero:
                 print("O número da linha não pode ser vazio. Tente novamente.")
                 continue
            break
        except EOFError:
            print("Entrada interrompida. Por favor, forneça um número.")
 
            continue
        except Exception:
            print("Ocorreu um erro na entrada. Tente novamente.")
            continue


    nome = input("Digite o nome da linha: ")

    
    while True:
        try:
            passageiros_str = input("Digite a quantidade de passageiros na hora de pico: ")
            passageiros = int(passageiros_str)
            if passageiros < 0:
                print("A quantidade de passageiros não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para passageiros.")
        except EOFError:
            print("Entrada interrompida. Por favor, forneça um número.")
            continue

    
    status_sobrecarregada = passageiros > LIMITE_MAXIMO

    
    linha_criada = {
        'numero': numero,
        'nome': nome,
        'passageiros': passageiros,
        'sobrecarregada': status_sobrecarregada
    }
    return linha_criada
print("=== INÍCIO DO GERENCIADOR DE LINHAS DE ÔNIBUS ===")


while True:
    print("\n--- Cadastro de Linha ---")

    
    linha_atual = cadastrar_linha()

    
    linhas.append(linha_atual)

    
    if linha_atual['sobrecarregada']:
        
        print(">> Linha sobrecarregada — adicionar mais ônibus")
      
        linhas_sobrecarregadas += 1
    else:
       
        print(">> Linha com demanda normal")

    
    try:
        continuar = input("\nDeseja cadastrar outra linha? (s/n): ").lower()
    except EOFError:
        
        continuar = 'n'
    except Exception:
        
        continuar = 'n'

   
    if continuar != "s":
        
        break


print("\n" + "="*8 + " RELATÓRIO FINAL " + "="*8)


print(f"Total de linhas analisadas: {len(linhas)}")


print(f"Linhas sobrecarregadas: {linhas_sobrecarregadas}")

print("\nDetalhes das Linhas:")


for item_linha in linhas:
    
    if item_linha['sobrecarregada']:
        
        status_texto = "SOBRECARREGADA"
    else:
        
        status_texto = "Normal"

   
    print(
        f" - Linha {item_linha['numero']} ({item_linha['nome']}): "
        f"{item_linha['passageiros']} passageiros — {status_texto}"
    )


print("\n=== FIM DO PROGRAMA ===")