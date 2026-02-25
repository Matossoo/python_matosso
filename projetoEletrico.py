print("=== CALCULADORA ELÉTRICA ===")

print("\nEscolha o cálculo:")
print("1 - Calcular Tensão (V)")
print("2 - Calcular Corrente (I)")
print("3 - Calcular Resistência (R)")
print("4 - Calcular Potência (P)")
print("5 - Calcular Consumo (kWh)")

opcao = input("Digite a opção: ")

if opcao == "1":
    r = float(input("Digite a resistência (Ohms): "))
    i = float(input("Digite a corrente (Amperes): "))
    v = r * i
    print("Tensão =", v, "Volts")

elif opcao == "2":
    v = float(input("Digite a tensão (Volts): "))
    r = float(input("Digite a resistência (Ohms): "))
    if r != 0:
        i = v / r
        print("Corrente =", i, "Amperes")
    else:
        print("Erro: resistência não pode ser zero!")

elif opcao == "3":
    v = float(input("Digite a tensão (Volts): "))
    i = float(input("Digite a corrente (Amperes): "))
    if i != 0:
        r = v / i
        print("Resistência =", r, "Ohms")
    else:
        print("Erro: corrente não pode ser zero!")

elif opcao == "4":
    v = float(input("Digite a tensão (Volts): "))
    i = float(input("Digite a corrente (Amperes): "))
    p = v * i
    print("Potência =", p, "Watts")

elif opcao == "5":
    p = float(input("Digite a potência do aparelho (Watts): "))
    t = float(input("Digite o tempo de uso (horas): "))
    consumo = (p * t) / 1000
    print("Consumo =", consumo, "kWh")

else:
    print("Opção inválida!")