from Cards import Cards

deck = Cards()

deck.shuffle_deck()

n = 100000
n2 = 20


for lol in range(n2):
    pairs = list()
    for i in range(n):
        (H1, H2) = (deck.draw(4), deck.draw(4))
        H01 = [H1[x][1] for x in range(len(H1))]
        H02 = [H2[x][1] for x in range(len(H2))]
        for c in H01:
            if c in H02:
                pairs.append(c)
                break

    print(len(pairs)/n)
    common = max(set(pairs), key=pairs.count)
    print(f'Most common pair: {common}')