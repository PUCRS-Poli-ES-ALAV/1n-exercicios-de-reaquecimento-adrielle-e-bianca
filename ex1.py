def multiplicacao_recursiva(a, b):
    """
    Multiplica dois números naturais usando somas sucessivas.
    
    Args:
        a: Primeiro número (quantidade de repetições)
        b: Segundo número (número a ser repetido na soma)
        
    Returns:
        O produto de a e b
    
    Exemplo:
        multiplicacao_recursiva(6, 4) = 4 + 4 + 4 + 4 + 4 + 4 = 24
    """
    # Caso base: se a for 0, o resultado é 0
    if a == 0:
        return 0
    
    # Caso recursivo: a * b = b + (a-1) * b
    return b + multiplicacao_recursiva(a - 1, b)

def main():
    """
    Função principal que solicita entrada do usuário e chama a função de multiplicação
    """
    print("Multiplicação por somas sucessivas")
    print("----------------------------------")
    
    try:
        # Solicita os números ao usuário
        a = int(input("Digite o primeiro número (a): "))
        b = int(input("Digite o segundo número (b): "))
        
        # Verifica se os números são naturais
        if a < 0 or b < 0:
            print("Por favor, digite apenas números naturais (maiores ou iguais a zero).")
            return
            
        # Calcula e exibe o resultado
        resultado = multiplicacao_recursiva(a, b)
        
        # Mostra o cálculo expandido
        if a > 0:
            expansao = " + ".join([str(b)] * a)
            print(f"{a} * {b} = {expansao} = {resultado}")
        else:
            print(f"{a} * {b} = 0")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")


if __name__ == "__main__":
    main()