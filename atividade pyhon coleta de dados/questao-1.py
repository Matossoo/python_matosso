import random

print("Monitoramento de Temperatura:\n")

for i in range(1, 21):
    temp = random.uniform(30, 100)
    
    print(f"Sensor {i}: {temp}°C")
    
    if temp > 80:
        print("Status: ⚠️ SUPERAQUECIMENTO!\n")
    else:
        print("Status: ✅ Temperatura normal\n")