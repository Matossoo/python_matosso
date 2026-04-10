import random

for i in range(1, 21):
    nivel = random.uniform(0,100)

    print(f"{i}° leitura do nível de água: {nivel:.2f}%")

    if nivel > 90 or nivel < 20:
        print("Status: Alerta de nível crítico\n")
    else:
        print("Status: Normal\n")