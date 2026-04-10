import random

for i in range(1, 6):
    temperatura = random.uniform(0, 20)

    print(f"{i}° leitura de temperatura: {temperatura:.2f}°C")

    if temperatura > 10:
        print("Status: Acima do limite\n")

        

