def pack_basket(basket,pile):
    charges = {0}
    for c in list(map(int, pile.replace('dust', '').split())):
        charges |= {c + d for d in charges if c + d <= basket}
    return 'The basket weighs %d kilograms' % max(charges)