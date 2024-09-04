def produto_bebida(): #função menu das escolhas de bebidas 
    while True:
        print("---- Bebidas ----")
        print("Digite (0) para voltar para o cardápio!")
        print("Digite (1) para Café -- 2,00 por xícara.")
        print("Digite (2) para Suco de laranja -- 3,50 por copo.")
        print("Digite (3) para Refrigerante -- 5,00 por lata.")
        print("Digite (4) para Chá gelado -- 4,00 por copo.")
        print("Digite (5) para Água mineral -- 1,50 por garrafa.\n")
        escolha = int(input("Qual sua escolha: "))

        if escolha == 0:
            return cardapio_menu()
        elif escolha == 1:
            quantidade = float(input("Quantas xícaras de Café você irá querer? "))
            preco = quantidade * 2.00
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 2:
            quantidade = float(input("Quantos copos de Suco de laranja você irá querer? "))
            preco = quantidade * 3.50
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 3:
            quantidade = float(input("Quantas latas de Refrigerante você irá querer? "))
            preco = quantidade * 5.00
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 4:
            quantidade = float(input("Quantos copos de Chá gelado você irá querer? "))
            preco = quantidade * 4.00
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 5:
            quantidade = float(input("Quantas garrafas de Água mineral você irá querer? "))
            preco = quantidade * 1.50
            print(f"Total a pagar: {preco:.2f}\n")
        else:
            print("Opção inválida! Tente novamente.\n")


def produto_doce(): #Função menu das escolhas dos doces
    while True:
        print("---- Doces ----")
        print("Digite (0) para voltar para o cardápio!")
        print("Digite (1) para Brigadeiro -- 1,50 por unidade.")
        print("Digite (2) para Beijinho -- 1,50 por unidade.")
        print("Digite (3) para Quindim -- 2,00 por unidade.")
        print("Digite (4) para Pudim -- 3,00 por fatia.")
        print("Digite (5) para Bolo de cenoura -- 2,50 por fatia.\n")
        escolha = int(input("Qual sua escolha: "))

        if escolha == 0:
            return cardapio_menu()
        elif escolha == 1:
            unidade = float(input("Quantas unidades de Brigadeiro você irá querer? "))
            preco = unidade * 1.50
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 2:
            unidade = float(input("Quantas unidades de Beijinho você irá querer? "))
            preco = unidade * 1.50
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 3:
            unidade = float(input("Quantas unidades de Quindim você irá querer? "))
            preco = unidade * 2.00
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 4:
            unidade = float(input("Quantas fatias de Pudim você irá querer? "))
            preco = unidade * 3.00
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 5:
            unidade = float(input("Quantas fatias de Bolo de cenoura você irá querer? "))
            preco = unidade * 2.50
            print(f"Total a pagar: {preco:.2f}\n")
        else:
            print("Opção inválida! Tente novamente.\n")


def produto_salgado(): #Função menu das escolhas dos salgados 
    while True:
        print("---- Salgados ----")
        print("Digite (0) para voltar para o cardápio!")
        print("Digite (1) para Coxinha -- 4,00 por unidade.")
        print("Digite (2) para Enroladinho -- 4,00 por unidade.")
        print("Digite (3) para Croquete -- 4,00 por unidade.")
        print("Digite (4) para Croissant -- 6,00 por unidade.")
        print("Digite (5) para Presunto e queijo -- 4,00 por unidade.")
        print("Digite (6) para Folheado -- 5,00 por unidade.\n")
        escolha = int(input("Qual sua escolha: "))

        if escolha == 0:
            return cardapio_menu()
        elif escolha == 1:
            unidade = float(input("Quantas unidades de Coxinha você irá querer? "))
            preco = unidade * 4.00
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 2:
            unidade = float(input("Quantas unidades de Enroladinho você irá querer? "))
            preco = unidade * 4.00
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 3:
            unidade = float(input("Quantas unidades de Croquete você irá querer? "))
            preco = unidade * 4.00
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 4:
            unidade = float(input("Quantas unidades de Croissant você irá querer? "))
            preco = unidade * 6.00
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 5:
            unidade = float(input("Quantas unidades de Presunto e queijo você irá querer? "))
            preco = unidade * 4.00
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 6:
            unidade = float(input("Quantas unidades de Folheado você irá querer? "))
            preco = unidade * 5.00
            print(f"Total a pagar: {preco:.2f}\n")
        else:
            print("Opção inválida! Tente novamente.\n")


def produto_pao(): #Função menu das escolhas dos pães
    while True:
        print("---- Pães ----")
        print("Digite (0) para voltar para o cardápio!")
        print("Digite (1) para Pão Francês -- 0,75 por unidade.")
        print("Digite (2) para Pão de leite -- 0,50 por unidade.")
        print("Digite (3) para Pão caseiro -- 0,50 por unidade.")
        print("Digite (4) para Pão Italiano -- 0,75 por unidade.")
        print("Digite (5) para Pão de queijo -- 0,50 por unidade.")
        print("Digite (6) para Pão doce -- 0,50 por unidade.\n")
        escolha = int(input("Qual sua escolha: "))

        if escolha == 0:
            return cardapio_menu()
        elif escolha == 1:
            unidade = float(input("Quantas unidades de Pão Francês você irá querer? "))
            preco = unidade * 0.75
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 2:
            unidade = float(input("Quantas unidades de Pão de leite você irá querer? "))
            preco = unidade * 0.50
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 3:
            unidade = float(input("Quantas unidades de Pão caseiro você irá querer? "))
            preco = unidade * 0.50
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 4:
            unidade = float(input("Quantas unidades de Pão Italiano você irá querer? "))
            preco = unidade * 0.75
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 5:
            unidade = float(input("Quantas unidades de Pão de queijo você irá querer? "))
            preco = unidade * 0.50
            print(f"Total a pagar: {preco:.2f}\n")
        elif escolha == 6:
            unidade = float(input("Quantas unidades de Pão doce você irá querer? "))
            preco = unidade * 0.50
            print(f"Total a pagar: {preco:.2f}\n")
        else:
            print("Opção inválida! Tente novamente.\n")


def cardapio_menu(): #Função menu príncipal - cardápio
    while True: #Laço de repetição do menu
        print("----------- Bem vindo ao sistema da padaria -------------")
        print("---- Cardápio ----")
        print("Digite (1) para escolher os pães")
        print("Digite (2) para escolher os salgados")
        print("Digite (3) para escolher os doces")
        print("Digite (4) para escolher as bebidas")
        print("Digite (0) caso queira sair do programa!")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 0:
            print("\nVocê escolheu sair do programa!")
            break
        elif opcao == 1:
            produto_pao()
        elif opcao == 2:
            produto_salgado()
        elif opcao == 3:
            produto_doce()
        elif opcao == 4:
            produto_bebida()
        else:
            print("Opção inválida! Tente novamente.\n")


# Inicializa o menu do cardápio
cardapio_menu()
