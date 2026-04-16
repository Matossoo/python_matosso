import random
eficiencia = []
for i in range(0, 10):

    eficiencia.append(random.randint(0, 100))
    print(f"Eficiência do equipamento {i+1}: {eficiencia[i]}%")

if sum(eficiencia) > 500:
        print(f"\nMeta atingida - {sum(eficiencia)}%\n")

print(f"\nmeta: 500%")
print(f"eficiencia total: {sum(eficiencia)}%")