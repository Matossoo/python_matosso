import random

for i in range(1, 21):
    c_e = random.uniform(10, 100)

    print(f"{i}° consumo energetico: {c_e:.2f}")

    if c_e > 50:
        print("Ultrapassou o limite.\n")
    else:
        print("Status: Consumo Normal\n")
