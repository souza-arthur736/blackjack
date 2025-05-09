import random
def calculo(hand, num_dict):
    total = 0 
    As = 0 
    for card in hand:
        rank = card[0]
        value = num_dict[rank]
        total += value
        if rank == 'A':
            As += 1 
    
    while As > 0 and total + 10 <= 21:
        total += 10
        As -= 1
    return total
num = {
    'A':1,
    'K':10,
    'Q':10,
    'J':10,
    '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2
}
naipe = {
    'S':1,
    'C':1,
    'D':1,
    'H':1
}
deck = []
start = input('Deseja jogar? S/N ').upper().replace(' ', '')

while start != 'N':
    #Constrói o deck e embaralha
    for value in num:
        for suit in naipe:
            deck.append(value + suit)
    random.shuffle(deck)
    
    #Dá as cartas para o player e dealer e printa na tela
    hand = [deck.pop() for _ in range(2)]
    print(f"Sua mão: {hand}")
    total = calculo(hand, num)
    print(f"Valor da sua mão: {total}")
    dealerhand = [deck.pop() for _ in range(2)]
    print('Mão do dealer: ?,' + dealerhand[1])
    totaldealer = calculo(dealerhand, num)
    
    #Rodada de fato
    jj = 0
    while total < 22:
        jj = input('Hit(h) ou Stand(s)? ')
        if jj == 'h':
            hand += [deck.pop()]
            total = calculo(hand, num)
            print(f"Sua mão: {hand}", f"\nTotal: {total}")
        if total > 21:
            print("Você estourou! Dealer vence.")
            break
        elif jj == 's':
            break
    if total <= 21:
        totaldealer = calculo(dealerhand, num)
        print(f"\nMão do dealer: {dealerhand}", f"\n Total: {totaldealer}")
        while totaldealer < 17:
            dealerhand += [deck.pop()]
            totaldealer = calculo(dealerhand, num)
            print(f"Dealer comprou: {dealerhand[-1]}", f"\n Total: {totaldealer}")
        if totaldealer > 21:
            print('Dealer estourou! Player vence.')
        elif totaldealer > total:
            print('Dealer ganhou em cima do player.')
        elif totaldealer < total:
            print('Player ganhou do dealer!')
        else:
            print('Empatados!')
    start = input('\n\nDeseja jogar novamente? S/N ').upper().replace(' ', '')
print('Encerrando o jogo...')
