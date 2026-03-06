#FUNÇÃO PARA LER A PRODUÇÃO
def producao(): 
    for i in range(0,5):
        while True:
            try:
                
                quantidade = int(input(f"\ndigite a quantidade produzida no periodo {i+1}: "))

                if quantidade <= 0:
                    print("Apenas valores positivos!")

                else:
                    lista.append(quantidade)
                    break
                
            except ValueError:
                    print("Valor errado. Tente novamente")

#CALCULAR O TOTAL PRODUZIDO
def total_produzido():
     total = sum(lista)
     print("Total produzido:", total)

#CALCULAR A MÉDIA
def média_produzida():
     media = sum(lista) / len(lista)
     print("Média de produção:", media)

#EXIBIR O MAIOR VALOR
def maior_valor():
     maior = max(lista)
     print("Maior valor:", maior)

#EXIBIR O MENOR VALOR
def menor_valor():
     menor = min(lista)
     print("Menor valor:", menor)

#FUNÇÃO ORGANIZADA PARA EXIBIR O RELATÓRIO
def relatorio():
     print("\n=====RELATÓRIO=====")
     print("Lsita:", lista)
     total_produzido()
     média_produzida()
     maior_valor()
     menor_valor()

#DEMONSTRAÇÃO DO CÓDIGO
while True:
    lista = []

    producao()
    relatorio()

    #PERMITIR QUE O USUÁRIO REPITA O PROCESSO 
    while True:

        opcao = input("\nDeseja executar novamente? (s/n): ").lower()


        if opcao == 's' or opcao == 'n':
            break

        else:
            print("Digite apenas (s) para sim ou (n) para não.")

    if opcao == 'n':
        print("Programa encerrado.")
        break