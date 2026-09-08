culturas = []
areas = []
insumos = []
litros = []
opcao = ""

while opcao != "5":
    print("1- Cadastrar Cultura")
    print("2- Listar Dados")
    print("3- Atualizar registro")
    print("4- Deletar registro")
    print("5- Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        print("Cadastrar Cultura")
        print("1- Café")
        print("2- Cana")
        tipo = input("Escolha do tipo: ")

        if tipo == "1":
            largura = float(input("Qual a largura: "))
            comprimento = float(input("Qual o comprimento: "))
            nome = "Cafe"
            area = largura * comprimento
        else:
            base = float(input("Qual a base: "))
            altura = float(input("Qual a altura: "))
            nome = "Cana"
            area = (base * altura) / 2
        insumo = input("Qual o nome do insumo? ")
        dose = float(input("Qual a dose em ml por m2: "))
        total_litros = (area * dose) / 1000

        culturas.append(nome)
        areas.append(area)
        insumos.append(insumo)
        litros.append(total_litros

        print(f"Cultura: {nome} - Area: {area:.2f} m2")
        print(f"Insumo: {insumo} - {total_litros:.2f} litros")
    elif opcao == "2":
        print("Listar Dados")
    elif opcao == "3":
        print("Atualizar registro")
    elif opcao == "4":
        print("Deletar registro")
    elif opcao == "5":
        print("Sair")
    else:
        print("Opcao invalida!")
