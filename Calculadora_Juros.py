# Cálculo de Juros: Simples e Compostos
# Juros simples: J = C * i * T
# Juros compostos: M = C * (1 + i)^T, onde J = M - C

def juros_simples(C, i, T):
    J = C * i * T
    M = C + J
    return J, M

def juros_compostos(C, i, T):
    M = C * (1 + i) ** T
    J = M - C
    return J, M

aux = True

while aux:
    print("\t\tCálculo de Juros")
    print("\nSelecione o tipo de cálculo:")
    print("(1) - Juros Simples")
    print("(2) - Juros Compostos")
    
    opc_calculo = int(input("Escolha uma opção (1 ou 2): "))
    
    if opc_calculo not in [1, 2]:
        print("Opção inválida. Tente novamente.")
        continue

    C = float(input("Montante inicial (C): "))
    print("\nQual o tipo de taxa?")
    print("(1) - mês\n(2) - bimestral\n(3) - trimestral\n(4) - semestral\n(5) - anual\n")
    
    opc_taxa = int(input("Escolha o tipo de taxa (1-5): "))

    if opc_taxa == 1:
        i = float(input("Valor da taxa ao mês (%): ")) / 100
        unidade = "meses"
    elif opc_taxa == 2:
        i = float(input("Valor da taxa bimestral (%): ")) / 100
        unidade = "bimestres"
    elif opc_taxa == 3:
        i = float(input("Valor da taxa trimestral (%): ")) / 100
        unidade = "trimestres"
    elif opc_taxa == 4:
        i = float(input("Valor da taxa semestral (%): ")) / 100
        unidade = "semestres"
    elif opc_taxa == 5:
        i = float(input("Valor da taxa anual (%): ")) / 100
        unidade = "anos"
    else:
        print("Opção inválida para o tipo de taxa.")
        continue

    T = float(input(f"Tempo em {unidade}: "))

    if opc_calculo == 1:
        J, M = juros_simples(C, i, T)
        print(f"\nCálculo de Juros Simples:")
    else:
        J, M = juros_compostos(C, i, T)
        print(f"\nCálculo de Juros Compostos:")

    print(f"Juros (J): R$ {J:.2f}")
    print(f"Montante Total (M = C + J): R$ {M:.2f}\n")

    # Perguntar se o usuário deseja calcular novamente
    continuar = input("Deseja realizar outro cálculo? (s/n): ").strip().lower()
    if continuar != 's':
        aux = False
