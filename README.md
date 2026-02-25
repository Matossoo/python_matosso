# python_matosso
🌐 Abridor de Navegador em Python
📌 Descrição

Este projeto é um programa simples desenvolvido em Python que permite abrir automaticamente o navegador padrão do computador através de um menu interativo no terminal.

O usuário pode escolher entre abrir sites pré-definidos ou inserir um link personalizado.

🚀 Funcionalidades

✅ Abrir Google

✅ Abrir YouTube

✅ Abrir site digitado pelo usuário

✅ Menu interativo

✅ Execução contínua até o usuário sair

🛠️ Tecnologias Utilizadas

Python 3

Biblioteca padrão webbrowser

📂 Estrutura do Projeto
abrir_navegador.py
README.md
💻 Como Executar

1️⃣ Instale o Python 3
2️⃣ Execute o arquivo no terminal:

python abrir_navegador.py
📜 Código Principal
import webbrowser

while True:
    print("\n=== MENU NAVEGADOR ===")
    print("1 - Abrir Google")
    print("2 - Abrir YouTube")
    print("3 - Abrir site personalizado")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        webbrowser.open("https://www.google.com")
    elif opcao == "2":
        webbrowser.open("https://www.youtube.com")
    elif opcao == "3":
        site = input("Digite o link completo: ")
        webbrowser.open(site)
    elif opcao == "0":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida!")
🎯 Objetivo do Projeto

Este projeto foi criado para praticar:

Estruturas de repetição (while)

Condicionais (if/elif)

Interação com o usuário via terminal

Uso de bibliotecas padrão do Python

👨‍💻 Autor

Rafael Fenilli Matosso
