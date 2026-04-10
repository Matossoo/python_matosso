import random

for i in range(1, 5):

    pressao = random.uniform(0,200)

    print(f"{i}° leitura da pressão: {pressao:.2f} kPa")

    if pressao > 120:
        print("Status: Pressão Alta\n")
    elif pressao < 80:
        print("Status: Pressão Baixa\n")
    else:
        print("Status: Pressão Normal\n")



        