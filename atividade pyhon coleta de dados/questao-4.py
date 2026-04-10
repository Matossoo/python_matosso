import random

for i in range (1,11):
    ph = random.uniform(0,14)

    print(f"{i}° leitura do pH: {ph:.2f}")

    if ph < 6 or ph > 8:
        print("Status: Ácido\n")
    else:
        print("Status: Ideal\n")
