from itertools import combinations

def main():
    total_players = 4
    players = total_players-1
    
    suits = ["s", "d", "c", "h"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    deck = []
    for suit in suits:
        for value in values:
            deck.append(Cards(value, suit))

    hand = []
    car = input("Enter the cards\n").split(",")
    for ca in car:   
        suit = ca[-1]
        value = ca[:-1]
        ca = Cards(value, suit)
        hand.append(ca)

    for i in hand:
        for j in deck:
            if i.value == j.value and i.suit == j.suit:
                deck.remove(j)

    # Calculating number of winning hands
    while True:
        w = 0
        combi = list(combinations(deck, 3))
        d = []
        hand = SortCard(hand)
        for i in hand:
            d.append(int(i.value))
            
        if check_hand(hand) == "Trial":
            for j in combi:
                if check_hand(j) == "Trial":
                    e = []
                    for k in j:
                        e.append(int(k.value))
                    if d[2] > e[2]:
                        w = w + 1
                else:
                    w = w + 1
        elif check_hand(hand) == "Colorrun":
            for j in combi:
                e = []
                if check_hand(j) == "Trial":
                    w = w + 0
                elif check_hand(j) == "Colorrun":
                    for k in j:
                        e.append(int(k.value))
                        e.sort
                    if d[2] > e[2]:
                        w = w + 1
                    elif d[2] == e[2]:
                        if d[1] > e[1]:
                            w = w + 1
                        elif d[1] == e[1]:
                            if d[0] > e[0]:
                                w = w + 1
                        else:
                            w = w + 0
                    else:
                        w = w + 0
                else:
                    w = w + 1
        elif check_hand(hand) == "Run":
            for j in combi:
                if check_hand(j) == "Trial" or check_hand(j) == "Colorrun":
                    w = w + 0
                elif check_hand(j) == "Run":
                    e = []
                    for k in j:
                        e.append(int(k.value))
                    e.sort
                    if d[2] > e[2]:
                        w = w + 1
                    elif d[2] == e[2]:
                        if d[1] > e[1]:
                            w = w + 1
                        elif d[1] == e[1]:
                            if d[0] > e[0]:
                                w = w + 1
                else:
                    w = w + 1
        elif check_hand(hand) == "Color":
            for j in combi:
                if (
                    check_hand(j) == "Trial"
                    or check_hand(j) == "Colorrun"
                    or check_hand(j) == "Run"
                ):
                    w = w + 0
                elif check_hand(j) == "Color":
                    e = []
                    for k in j:
                        e.append(int(k.value))
                        e.sort
                    if d[2] > e[2]:
                        w = w + 1
                    elif d[2] == e[2]:
                        if d[1] > e[1]:
                            w = w + 1
                        elif d[1] == e[1]:
                            if d[0] > e[0]:
                                w = w + 1
                else:
                    w = w + 1
        elif check_hand(hand) == "Pair":
            for j in combi:
                e = []
                if (
                    check_hand(j) == "Trial"
                    or check_hand(j) == "Colorrun"
                    or check_hand(j) == "Run"
                    or check_hand(j) == "Color"
                ):
                    w = w + 0
                elif check_hand(j) == "Pair":
                    e = []
                    for k in j:
                        e.append(int(k.value))
                        e.sort
                    if d[0] == d[1]:
                        if e[0] == e[1]:
                            if d[0] > e[0]:
                                w = w + 1
                            elif d[0] == e[0]:
                                if d[2] > e[2]:
                                    w = w + 1
                        elif e[1] == e[2]:
                            if d[0] > e[1]:
                                w = w + 1
                            elif d[0] == e[1]:
                                if d[2] > e[0]:
                                    w = w + 1
                    elif d[1] == d[2]:
                        if e[0] == e[1]:
                            if d[2] > e[0]:
                                w = w + 1
                            elif d[2] == e[0]:
                                if d[0] > e[2]:
                                    w = w + 1
                        elif e[1] == e[2]:
                            if d[2] > e[1]:
                                w = w + 1
                            elif d[2] == e[1]:
                                if d[0] > e[0]:
                                    w = w + 1
                else:
                    w = w + 1
        elif check_hand(hand) == "Top":
            for j in combi:
                if check_hand(j) == "Top":
                    e = []
                    for k in j:
                        e.append(int(k.value))
                        e.sort
                    if d[2] > e[2]:
                        w = w + 1
                    elif d[2] == e[2]:
                        if d[1] > e[1]:
                            w = w + 1
                        elif d[1] == e[1]:
                            if d[0] > e[0]:
                                w = w + 1

        print(check_hand(hand))
        print(w)
        print(len(combi))
        win = ((w / len(combi)) ** players) * 100
        print(win)
        nca = input("Enter the cards to remove from play\n").split(",")
        if nca == "n":
            main()
        
        ncar = []
        for nc in nca:
            nsuit = nc[-1]
            nvalue = nc[:-1]
            ncar.append(Cards(nvalue, nsuit))
            
        for i in ncar:
            for j in deck:
                if i.value == j.value and i.suit == j.suit:
                    deck.remove(j)
                        
            

def check_trial(lis0):
    a = []
    for k in lis0:
        a.append(k.value)

    if a[0] == a[1] and a[1] == a[2]:
        return True


def check_colorrun(lis1):
    if check_run(lis1) == True and check_color(lis1) == True:
        return True


def check_run(lis2):
    a = []
    b = 0
    for k in lis2:
        b = b + 1
        a.append(int(k.value))
        if b == 3:
            a.sort()
            if a[0] == 2 and a[1] == 3 and a[2] == 14:
                return True
            elif a[0] + 1 == a[1] and a[1] + 1 == a[2]:
                return True


def check_color(lis3):
    a = []
    for k in lis3:
        a.append(k.suit)
    if a[0] == a[1] and a[1] == a[2]:
        return True


def check_pair(lis4):
    b = 0
    a = []
    for k in lis4:
        b = b + 1
        a.append(int(k.value))
        if b == 3:
            a.sort()
            if a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
                return True


def check_hand(lis5):
    if check_trial(lis5) == True:
        handtype1 = "Trial"
        return handtype1
    elif check_colorrun(lis5) == True:
        handtype1 = "Colorrun"
        return handtype1
    elif check_run(lis5) == True:
        handtype1 = "Run"
        return handtype1
    elif check_color(lis5) == True:
        handtype1 = "Color"
        return handtype1
    elif check_pair(lis5) == True:
        handtype1 = "Pair"
        return handtype1
    else:
        handtype1 = "Top"
        return handtype1
    
def SortCard(hand):
    hand.sort(key=lambda x: x.value)
    return hand


class Cards:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def card(self):
        return (value, suit)
    
if __name__ == "__main__":
    main()