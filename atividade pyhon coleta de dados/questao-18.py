import random

for i in range(0,100):
    leitura = random.randint(0,100)

    if leitura > 80:
        print(f"Alerta: Leitura anômala detectada - {leitura}\n")



