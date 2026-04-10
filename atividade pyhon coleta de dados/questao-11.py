import random

cont = 0

for i in range(1, 21):

    valor = random.randint(0,10)

    print(f"{i}° leitura do sensor: {valor}")

    if valor > 7:
        print("ALARME\n")
        cont += 1
    else:
        print("Normal.\n")

print(f"Total de alarmes: {cont}")