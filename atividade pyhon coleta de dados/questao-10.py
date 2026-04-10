import random


for i in range(0,1):

    temperatura = random.uniform(30, 100)

    print(f"{i+1}° leitura de temperatura: {temperatura:.2f}°C")

    if temperatura > 80:
        print("Status: ⚠️  SUPERAQUECIMENTO!\nMAQUINA DELIGADA!\n")
    else:
        print("Status: ✅ Temperatura normal\n")