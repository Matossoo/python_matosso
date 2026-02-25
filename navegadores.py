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