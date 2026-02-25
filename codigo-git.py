import random
import time

print("=" * 40)
print("🎮  BEM-VINDO AO JOGO DE ADIVINHAÇÃO  🎮")
print("=" * 40)

nome = input("Digite seu nome: ")
print(f"\nBoa sorte, {nome}!")
time.sleep(1)

print("\nEscolha a dificuldade:")
print("1 - Fácil (1 a 10)")
print("2 - Médio (1 a 50)")
print("3 - Difícil (1 a 100)")

nivel = int(input("Digite o nível: "))

if nivel == 1:
    numero_secreto = random.randint(1, 10)
    tentativas = 5
elif nivel == 2:
    numero_secreto = random.randint(1, 50)
    tentativas = 7
else:
    numero_secreto = random.randint(1, 100)
    tentativas = 10

print("\n🔎 Estou pensando em um número...")
time.sleep(1)

pontos = 100

while tentativas > 0:
    chute = int(input("\nDigite seu palpite: "))
    
    if chute == numero_secreto:
        print(f"\n🎉 PARABÉNS {nome.upper()}! Você acertou!")
        print(f"🏆 Sua pontuação final foi: {pontos}")
        break
    elif chute > numero_secreto:
        print("📉 Muito alto!")
    else:
        print("📈 Muito baixo!")
    
    tentativas -= 1
    pontos -= 10
    print(f"❌ Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("\n💀 Você perdeu!")
    print(f"O número era {numero_secreto}")