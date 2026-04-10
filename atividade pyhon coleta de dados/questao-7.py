import random

print("Monitoramento de Nível de Vibração:\n")

for i in range(1, 11):

    dados = random.uniform(0, 100)

    print(f"{i}° leitura do nível de vibração: {dados:.2f}%")

    if dados > 60:
        print("Status: Alerta de vibração acima do limite\n")
    else:
        print("Status: Normal\n")