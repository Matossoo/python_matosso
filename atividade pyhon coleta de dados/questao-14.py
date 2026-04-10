
dados = []

for i in range(0,5):
    dados.append(int(input(f"{i+1}° leitura do sensor (Digite um valor entre 0 e 100): ")))


print(dados)

media = sum(dados) / len(dados)
print(f"Media das leituras: {media:.2f}")
