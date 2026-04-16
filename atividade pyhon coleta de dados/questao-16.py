import random

for i in range(0,4):
    leitura = random.randint(0,10)

    print(f"{i+1}° leitura do sensor: {leitura}\n")
print("Enviando dados para a nuvem...\n")
print("Dados enviados com sucesso!")