import random
def calculo(hand):
    aces = 0 
    handvalues = []
    for x in hand:
        value = x[0]
        try:
            int_value = int(value)
        except ValueError:
            if value == 'A':
                int_value = 11
                aces += 1
            else:
                int_value = 10
        handvalues.append(int_value)
    total = sum(handvalues)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total
num = ['K', 'Q', 'J', '9', '8', '7', '6', '5', '4','3','2','A']
naipe = ['♠', '♥', '♦', '♣']
deck = []
valuedeck = []

Start = input('Deseja jogar? Digite qualquer botão | (X) para sair').upper()
while Start != 'X':
    for value in num:
        for suit in naipe:
            deck.append(value + suit)
    random.shuffle(deck)

    hand = [deck.pop() for _ in range (2)]
    dealerhand = [deck.pop() for _ in range(2)]

    total = calculo(hand)
    dealertotal = calculo(dealerhand)
    print(f"\nSua mão: {hand}", f" | Total: {total}")
    print('Mão do dealer: ?', dealerhand[-1])
    jj = 0
    while total < 22:
        jj = input('Hit(1) ou Stand(2)?').lower().replace(' ', '')
        if jj == '1':
            hand += [deck.pop()]
            total = calculo(hand)
            print(f"\nSua mão: {hand}", f" | Total: {total}")
        if total > 21:
            print("\nVocê estourou! Dealer vence.")
            break
        elif jj == '2':
            break
    if total <= 21:
        dealertotal = calculo(dealerhand)
        print(f"Mão do dealer: {dealerhand}", f" | Total: {dealertotal}")
        while dealertotal < 17:
            dealerhand += [deck.pop()]
            dealertotal = calculo(dealerhand)
            print(f"Dealer sacou: {dealerhand[-1]}", f" | Total: {dealertotal}")
        if dealertotal > 21:
            print('\nDealer estourou! Player vence.')
        elif dealertotal > total:
            print('\nDealer ganhou em cima do player.')
        elif dealertotal < total:
            print('\nPlayer ganhou do dealer!')
        else:
            print('Empatados!')
    Start = input('\nDeseja jogar novamente? Digite qualquer botão | (X) para sair').upper().replace(' ', '')
print('Encerrando o jogo...')
