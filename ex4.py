def inverter_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + inverter_string(s[:-1])

def main():
    """
    Função principal que solicita entrada do usuário e chama a função de soma recursiva
    """
    print("Inverter string")
    print("-------------------------------")
    
    try:
        x = str(input("Digite a string: "))
        
        if not isinstance(x, str):
            print("Por favor, digite apenas strings")
            return
            
        resultado = inverter_string(x)
        print(resultado)
            
    except ValueError:
        print("Entrada inválida. Por favor, digite uma string.")


if __name__ == "__main__":
    main()
