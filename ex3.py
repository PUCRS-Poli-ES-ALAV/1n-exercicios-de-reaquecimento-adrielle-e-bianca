def soma_harmonica(n, termo=1, expressao="1"):
    if termo == n:
        return expressao + f" + 1/{termo}"
    return soma_harmonica(n, termo + 1, expressao + f" + 1/{termo}")

def main():
    """
    Função principal que solicita entrada do usuário e chama a função de soma recursiva
    """
    print("Soma harmonica")
    print("-------------------------------")
    
    try:
        # Solicita os números ao usuário
        x = int(input("Digite o primeiro número (n): "))
        
        if x <= 0:
            print("Por favor, digite apenas números maiores que 0.")
            return
            
        resultado = soma_harmonica(x)
        print(resultado)
            
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")


if __name__ == "__main__":
    main()