import random
dados = []
for i in range(0,10):

    dados.append(random.randint(0,10))
    print(f"Leitura do sensor {i+1}: {dados[i]}")

print(f"relatório final: {dados}")

