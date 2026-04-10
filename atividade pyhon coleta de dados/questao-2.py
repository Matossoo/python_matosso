import random

for i in range(0,20):
    velocidade = random.uniform(0.1, 2)

    print(f"leitura {i+1}: {velocidade:.2f} m/s")

    if velocidade > 0.6:
        print("Status: Normal\n")
    else:
        print("Status: Baixa Velocidade\n")