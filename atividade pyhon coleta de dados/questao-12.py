import random

for i in range(20):
    classifique = random.uniform(0, 10)

    print(f"{i+1}° leitura de classificação: {classifique:.2f}")

    if classifique < 4:
        print("Alerta")
    elif classifique > 7:
        print("Critico")
    else:
        print("Normal")