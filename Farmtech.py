culturas = []
areas = []
insumos = []
litros = []
#Até aqui eu abri as listas necessárias
opcao = ""
#as aspas coladas indicam um texto vazio

import csv
#biblioteca padrao do Python para gravar/ler arquivos CSV
#usada aqui so na opcao de exportar os dados para o R

def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor invalido. Digite um numero (ex: 10 ou 10.5).")

def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor invalido. Digite um numero inteiro.")
#funcoes que ficam pedindo o valor de novo enquanto o usuario nao digitar um numero valido
#assim o programa nao quebra com ValueError quando alguem digita texto no lugar de numero

def exportar_csv(caminho="dados_farmtech.csv"):
    with open(caminho, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["cultura", "area_m2", "insumo", "litros"])
        for i in range(len(culturas)):
            escritor.writerow([culturas[i], areas[i], insumos[i], litros[i]])
    print(f"Dados exportados para '{caminho}'. Agora e so rodar o estatisticas.R.")
#percorre as 4 listas na mesma posicao i e escreve uma linha por registro
#esse arquivo e o que o script em R vai ler para calcular media e desvio padrao

while opcao != "6":
    print("")
    print("=" * 45)
    print("   FARMTECH SOLUTIONS - GESTAO DE PLANTIO")
    print("=" * 45)
    print("CADASTRO E CALCULO")
    print("  1- Cadastrar Cultura")
    print("-" * 45)
    print("CONSULTA E EDICAO")
    print("  2- Listar Dados")
    print("  3- Atualizar registro")
    print("  4- Deletar registro")
    print("-" * 45)
    print("EXPORTACAO E SAIDA")
    print("  5- Exportar dados para CSV (uso no R)")
    print("  6- Sair")
    print("=" * 45)
    opcao = input("Escolha uma opcao: ")
#Usando while que faz o código rodar sem parar, equanto for verdadeira, só para quando for falsa
#serve para criar  por exemplo  o menu
#o "Sair" virou opcao 6 porque a nova opcao 5 (exportar) entrou no meio
    match opcao:

        case "1":
            print("")
            print("--- CADASTRAR CULTURA ---")
            print("1- Café")
            print("2- Cana")
            tipo = input("Escolha do tipo: ")
#poderia ter usado o elif em tudo, decidi usar o match case para abordar o capítulo 5.
# essa estrutura serve para testar igualdade, ele não serve para maior ou menor

            if tipo == "1":
                largura = ler_float("Qual a largura: ")
                comprimento = ler_float("Qual o comprimento: ")
                nome = "Cafe"
                area = largura * comprimento
#se for o tipo 1 o café ele segue com o cálculo específico dessa modalidade. Usa float
#porque é um número com casas decimais
            else:
                base = ler_float("Qual a base: ")
                altura = ler_float("Qual a altura: ")
                nome = "Cana"
                area = (base * altura) / 2
#como só tem duas culturas qualquer outra coisa diferente do café só pode ser a cana
#ele segue com o cálculo da cana que é diferente da do café

            insumo = input("Qual o nome do insumo? ")
            dose = ler_float("Qual a dose em ml por m2: ")
            total_litros = (area * dose) / 1000
#transforma a variável dose em número com casas decimais
#aplica a fórmula e transforma mililitros em litros

            culturas.append(nome)
            areas.append(area)
            insumos.append(insumo)
            litros.append(total_litros)
#aqui o comando append salva todos os registros para que não sejam substituídos

            print("-" * 30)
            print(f"Cultura: {nome} - Area: {area:.2f} m2")
            print(f"Insumo: {insumo} - {total_litros:.2f} litros")
            print("Registro cadastrado com sucesso!")
#quando coloca o f na frente permite que ele fique atento a variáveis dentro das chaves
#o .2f é estético, define o número de casas decimais apresentados

        case "2":
            print("")
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
            print("")
            print("--- ATUALIZAR REGISTRO ---")

            if len(culturas) == 0:
                print("Nenhum registro cadastrado")

            else:
                for i in range(len(culturas)):
                    print(f"{i} | {culturas[i]} | {areas[i]:.2f} m2 | {insumos[i]} | {litros[i]:.2f} L")

                indice = ler_int("Qual numero deseja atualizar? ")
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
                        largura = ler_float("Qual a largura: ")
                        comprimento = ler_float("Qual o comprimento: ")
                        nome = "Cafe"
                        area = largura * comprimento
#se for café (item 1) ele faz o cálculo específico do café
                    else:
                        base = ler_float("Qual a base: ")
                        altura = ler_float("Qual a altura: ")
                        nome = "Cana"
                        area = (base * altura) / 2
#Qualquer outra coisa é Cana e ele faz o cálculo específico dessa categoria

                    insumo = input("Qual o nome do insumo? ")
                    dose = ler_float("Qual a dose em ml por m2: ")
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
            print("")
            print("--- DELETAR REGISTRO ---")

            if len(culturas) == 0:
                print("Nenhum registro cadastrado")

            else:
                for i in range(len(culturas)):
                    print(f"{i} | {culturas[i]} | {areas[i]:.2f} m2 | {insumos[i]} | {litros[i]:.2f} L")

                indice = ler_int("Qual numero deseja deletar? ")
#mesma logica da atualizacao: mostra a lista e pede a posicao a remover

                if indice >= 0 and indice < len(culturas):
                    culturas.pop(indice)
                    areas.pop(indice)
                    insumos.pop(indice)
                    litros.pop(indice)
#pop remove o item da posicao indicada e desloca os seguintes, ao contrario do
#update ele nao troca o conteudo, ele apaga a posicao inteira

                    print("Registro deletado com sucesso.")

                else:
                    print("Numero invalido.")

        case "5":
            print("")
            print("--- EXPORTAR PARA CSV ---")
            exportar_csv()
#chama a funcao que grava as 4 listas em dados_farmtech.csv
#esse arquivo e o que os scripts estatisticas.R e clima.R vao usar depois

        case "6":
            print("")
            print("Encerrando o FarmTech. Ate a proxima!")

        case _:
            print("Opcao invalida!")
#case _ é o "qualquer outra coisa", equivale ao else do if/elif
