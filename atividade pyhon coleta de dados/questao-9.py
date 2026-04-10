import random

print("lista de produção por hora:\n")


producao = []

for i in range(1, 25):
    producao.append(random.randint(1, 100))
    print(f"horario: {i:.2f}: {producao[-1]} unidades")


media = sum(producao) / len(producao)
print(f"\nProdução média: {media:.2f} unidades")

if media > 50:
    print("\nMeta atingida\n")
else:
    print("\nMeta não atingida\n")
