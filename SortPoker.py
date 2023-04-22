import random
import math

listCards = ["2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "th", "jh", "qh", "kh", "ah",
             "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "tc", "jc", "qc", "kc", "ac",
             "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "ts", "js", "qs", "ks", "as",
             "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "td", "jd", "qd", "kd", "ad"]

listRank = ["2", "3", "4", "5", "6", "7", "8", "9", "t", "j", "q", "k", "a"]

dictCards = {}
dictRank = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "t": 10, "j": 11, "q": 12, "k": 13, "a": 14}


def dealCards(deck, n):
    listDeals = []

    for i in range(0, n):
        index = 64
        while index not in dictCards:
            index = random.randrange(0, 51)

        listDeals.append(deck[index])
        del deck[index]

    return listDeals


# end def

def init():
    i = 0
    for card in listCards:
        dictCards[i] = card
        i += 1

# end def


def merge(ar, p, q, r):
    # Merge 2 sorted array into one
    nL = q - p + 1
    nR = r - q

    arLeft = ar[p:q + 1]
    arRight = ar[q + 1:r + 1]

    i = 0
    j = 0
    k = p

    while i < nL and j < nR:
        if getRank(arLeft[i]) <= getRank(arRight[j]):
            ar[k] = arLeft[i]
            i += 1
        else:
            ar[k] = arRight[j]
            j += 1

        k = k + 1

    while i < nL:
        ar[k] = arLeft[i]
        i = i + 1
        k = k + 1

    while j < nR:
        ar[k] = arRight[j]
        j = j + 1
        k = k + 1


# end def


def mergeSort(ar, p, r):
    if p >= r:
        return
    q = math.floor((p + r) / 2)
    mergeSort(ar, p, q)
    mergeSort(ar, q + 1, r)
    merge(ar, p, q, r)

# end def


def getRank(card):
    rank = dictRank.get(card[:1])

    return rank

#end def


init()
print("\nWelcome to Poker sort...")
print("==============================")

ncard = int(input("\nEnter the number of cards for an Random generate hand: "))

while(ncard < 0 or ncard > 51):
    ncard = int(input("\nEnter the number of cards for an Random generate hand: "))

list1 = dealCards(dictCards, ncard)
print("\nYour hand is ")
print(list1)
#print(getRank(list1[0]))

mergeSort(list1, 0, ncard-1)
print("\nYour hand after the sort is ")
print(list1)


