culturas = []
areas = []
insumos = []
litros = []
#Até aqui eu abri as listas necessárias
opcao = ""
#as aspas coladas indicam um texto vazio
while opcao != "5":
    print("1- Cadastrar Cultura")
    print("2- Listar Dados")
    print("3- Atualizar registro")
    print("4- Deletar registro")
    print("5- Sair")
    opcao = input("Escolha: ")
#Usando while que faz o código rodar sem parar, equanto for verdadeira, só para quando for falsa
#serve para criar  por exemplo  o menu
    match opcao:

        case "1":
            print("Cadastrar Cultura")
            print("1- Café")
            print("2- Cana")
            tipo = input("Escolha do tipo: ")
#poderia ter usado o elif em tudo, decidi usar o match case para abordar o capítulo 5.
# essa estrutura serve para testar igualdade, ele não serve para maior ou menor

            if tipo == "1":
                largura = float(input("Qual a largura: "))
                comprimento = float(input("Qual o comprimento: "))
                nome = "Cafe"
                area = largura * comprimento
#se for o tipo 1 o café ele segue com o cálculo específico dessa modalidade. Usa float
#porque é um número com casas decimais
            else:
                base = float(input("Qual a base: "))
                altura = float(input("Qual a altura: "))
                nome = "Cana"
                area = (base * altura) / 2
#como só tem duas culturas qualquer outra coisa diferente do café só pode ser a cana
#ele segue com o cálculo da cana que é diferente da do café

            insumo = input("Qual o nome do insumo? ")
            dose = float(input("Qual a dose em ml por m2: "))
            total_litros = (area * dose) / 1000
#transforma a variável dose em número com casas decimais
#aplica a fórmula e transforma mililitros em litros

            culturas.append(nome)
            areas.append(area)
            insumos.append(insumo)
            litros.append(total_litros)
#aqui o comando append salva todos os registros para que não sejam substituídos

            print(f"Cultura: {nome} - Area: {area:.2f} m2")
            print(f"Insumo: {insumo} - {total_litros:.2f} litros")
#quando coloca o f na frente permite que ele fique atento a variáveis dentro das chaves
#o .2f é estético, define o número de casas decimais apresentados

        case "2":
            print("--- REGISTROS CADASTRADOS ---")
            if len(culturas) == 0:
                print("Nenhum registro cadastrado")
            else:
                for i in range(len(culturas)):
                    print(f"{i} | {culturas[i]} | {areas[i]:.2f} m2 | {insumos[i]} | {litros[i]:.2f} L")
#agora na opção 2 o comando len conta quantas culturas, se o número for 0 ele apresenta
#mensagem de nenhum registro. Else, qualquer coisa diferente de zero dentro de cultura ele mostra
#a variável i indica a posição da vez, que vai na sequencia do range
#e mostra o conteúdo de cada lista naquela posição

        case "3":
            print("--- ATUALIZAR REGISTRO ---")

            if len(culturas) == 0:
                print("Nenhum registro cadastrado")

            else:
                for i in range(len(culturas)):
                    print(f"{i} | {culturas[i]} | {areas[i]:.2f} m2 | {insumos[i]} | {litros[i]:.2f} L")

                indice = int(input("Qual numero deseja atualizar? "))
#depois de mostrar a lista, ele pergunta qual registro o usuario quer mudar
#cria a variavel indice e guarda ali o numero digitado
#esse numero é a posicao do registro na lista, nao é opcao de menu
#usa int porque posicao de lista é sempre numero inteiro, nao existe gaveta 1.5

                if indice >= 0 and indice < len(culturas):
#confere se o numero digitado existe na lista
#precisa das duas condicoes: nao pode ser negativo e nao pode passar da ultima posicao
#sem esse teste o programa quebra com IndexError

                    print("1- Café")
                    print("2- Cana")
                    tipo = input("Escolha do tipo: ")
#apresenta as opções em tela e pede para o usuário escolher

                    if tipo == "1":
                        largura = float(input("Qual a largura: "))
                        comprimento = float(input("Qual o comprimento: "))
                        nome = "Cafe"
                        area = largura * comprimento
#se for café (item 1) ele faz o cálculo específico do café
                    else:
                        base = float(input("Qual a base: "))
                        altura = float(input("Qual a altura: "))
                        nome = "Cana"
                        area = (base * altura) / 2
#Qualquer outra coisa é Cana e ele faz o cálculo específico dessa categoria

                    insumo = input("Qual o nome do insumo? ")
                    dose = float(input("Qual a dose em ml por m2: "))
                    total_litros = (area * dose) / 1000

                    culturas[indice] = nome
                    areas[indice] = area
                    insumos[indice] = insumo
                    litros[indice] = total_litros
#aqui ele troca o conteudo antigo pelo novo, nas 4 listas
#o indice diz em qual posicao trocar. se o usuario digitou 1, troca na posicao 1
#é diferente do append: o append cria uma posicao nova no fim,
#esse aqui só substitui o que ja estava naquela posicao

                    print("Registro atualizado com sucesso.")

                else:
                    print("Numero invalido.")
#este else responde ao if do indice, por isso fica alinhado com ele
#cai aqui quando o numero digitado nao existe na lista

        case "4":
            print("Deletar registro")

        case "5":
            print("Sair")

        case _:
            print("Opcao invalida!")
#case _ é o "qualquer outra coisa", equivale ao else do if/elif