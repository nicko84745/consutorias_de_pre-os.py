# exibe os codigos disponiveis
print("codigos de produto:")
print("1 - cafe")
print('2 - chá')
print('3 - suco')
print('4 - refrigerante')
print('5 - água')
print('0 - sair')

# solicite o codigo do produto ao usuario
codigo = int(input("digite o codigo do produto: "))

# usa match-case para mostrar o preço com base no codigo
match codigo:
    case 1:
        print("produto: café - preço: R$ 4,50")
    case 2:
        print("produto: chá - preço: R$ 3,00")
    case 3:
        print("produto: suco - preço: R$ 5,00")
    case 4:
        print("produto: refrigersnte - preço: R$ 6,00")
    case 5:
        print("produto: água - preço: R$ 2,00")
    case 0:
        print("saindo do programa...")
        exit() # Emcerra o programa se o codigo for 0  
    case _:
        print("codigo invalido. por favor, tente novamente")        