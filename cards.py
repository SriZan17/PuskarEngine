from itertools import combinations

suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]


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


class Cards:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def card(self):
        return (value, suit)


# Getting all possible combination of cards
deck = []
for suit in suits:
    for value in values:
        deck.append(Cards(value, suit))
comb = combinations(deck, 3)
combi = list(comb)

# Taking inputs from user
players = int(input("Enter no. of players besides you\n"))
hand = []
for i in range(0, 3):
    value = input("Enter the value of card\n")
    suit = input("Enter the suit of card\n")
    ca = Cards(value, suit)
    hand.append(ca)

# Removing combinations which are impossible
for i in hand:
    for j in combi:
        for k in j:
            if k.value == i.value and k.suit == i.suit:
                combi.remove(j)

c = 0
d = []
for l in hand:
    d.append(int(l.value))
d.sort

# Calculating number of winning hands
while True:
    w = 0
    if check_hand(hand) == "Trial":
        for j in combi:
            if check_hand(j) == "Trial":
                e = []
                for k in j:
                    e.append(int(k.value))
                if d[2] > e[2]:
                    w = w + 1
                else:
                    w = w + 0
            else:
                w = w + 1
    elif check_hand(hand) == "Colorrun":
        for j in combi:
            e = [0]
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
    nvalue = input("Enter the value of card to remove from play\n")
    nsuit = input("Enter the suit of card to remove from play\n")
    ca = Cards(nvalue, nsuit)
    for j in combi:
        for k in j:
            if k.value == ca.value and k.suit == ca.suit:
                combi.remove(j)
