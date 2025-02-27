def soma_recursiva(a, b, expr=None, count=1):
    if expr is None:
        expr = f"{a} + {b} ="
    
    if b == 0:
        return expr + " (" + "+ " * count + "1))"
    
    return soma_recursiva(a + 1, b - 1, expr + " +", count + 1)


def main():
    """
    Função principal que solicita entrada do usuário e chama a função de soma recursiva
    """
    print("Soma por incrementos sucessivos")
    print("-------------------------------")
    
    try:
        # Solicita os números ao usuário
        a = int(input("Digite o primeiro número (a): "))
        b = int(input("Digite o segundo número (b): "))
        
        # Verifica se os números são naturais
        if a < 0 or b < 0:
            print("Por favor, digite apenas números naturais (maiores ou iguais a zero).")
            return
            
        resultado = soma_recursiva(a, b)

        if b > 0:
            print(resultado)
        else:
            print(f"{a} + {b} = {a}")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")


if __name__ == "__main__":
    main()