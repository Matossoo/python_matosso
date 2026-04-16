import random
dados = []

for i in range(0,5):
    dados.append(int(random.randint(0,100)))

    print(f"{i+1}° leitura do sensor: {dados[i]}")

media = sum(dados) / len(dados)
print(f"Media das leituras: {media:.2f}")

print(f"Valor máximo: {max(dados)}")
print(f"Valor mínimo: {min(dados)}")