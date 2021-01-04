

#EXEMPLO - ESTOQUE DE MERCADO

estoque={'Banana': [45,2.20],
        'Laranja': [48,3],
        'Limão': [28,1.80],
        'Maçã': [29, 3.65],
        'Uva': [112,6.50]}


##################

opcao=0
while opcao != 7:
    print('''           1 - Vender
           2 - Adicionar fruta ao estoque
           3 - Remover Fruta do estoque
           4 - Listar estoque
           5 - Listar estoque completo
           6 - Alterar estoque
           7 - Sair do programa''')
    opcao = int(input('Qual é sua opção'))
    if opcao == 1:
        for nome, qt_valor in estoque.items():
            print('Nome: ', nome)
            print('Quantidade: ', qt_valor[0], 'kg disponíveis')
            print('Preco: R$', qt_valor[1], '/kg')
        escolha = (int(input('Digite o nome da fruta que deseja: ' )))
    elif opcao == 2:
        estoque[key] = (input('Digite o nome da fruta que quer adicionar: '))
        print('Digite quantos KG da fruta irá inserir: ', qt_valor[0])
        qt_valor.append[0]
        print('Qual o valor por KG da fruta ', qt_valor[1])
        qt_valor.append[1]
    elif opcao == 3:
        del (estoque[input('Digite o nome da fruta que quer remover: ')])
        print('Fruta removida')
    elif opcao == 4:
        for k in estoque.keys():
            print(k)
    elif opcao == 5:
        for nome, qt_valor in estoque.items():
            print('Nome: ', nome)
            print('Quantidade: ', qt_valor[0], 'kg disponíveis')
            print('Preco: R$', qt_valor[1], '/kg')
    elif opcao == 6:
        
    else:
        print('Opção inválida. Tente novamente')