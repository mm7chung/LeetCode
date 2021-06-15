from math import log
import random
import time

deckList = []
suitList = ['C', 'D', 'H', 'S']
# make a list
# make a string with numbers 1-13 + suit(C D H S)
# append list with strings



for element in suitList:
    for deckNum in range(1,14):
        deckList.append(str(deckNum) + element)

def createList():
    shuffleList = []
    while len(shuffleList) < 52:
        number = random.randint(1,52)
        if number not in shuffleList:
            shuffleList.append(number)
    return shuffleList

shuffleList = createList()

newdeckList = []
for element in shuffleList:
    newdeckList.append(deckList[element-1])


card = "5D"
card2 = "12D"

def parseNumberAndSuit(card):
    value = int(card[:-1])
    suit = card[-1]
    return value, suit

def convertValue(value, suit):
    if suit == 'C':
        value += 0
    elif suit == 'D':
        value += 13
    elif suit == 'H':
        value += 26
    else:
        value += 39
    return  value

def sort(unorderedList):
    orderedList = []
    for element in unorderedList:
        positionToInsert = len(orderedList)
        for idx in range(0, len(orderedList)):
            if element < orderedList[idx]:
                positionToInsert = idx
                break
        orderedList.insert(positionToInsert, element)
    return orderedList

value, suit = parseNumberAndSuit(card)

unorderedList = []
for element in newdeckList:
    value, suit = parseNumberAndSuit(element)
    trueValue = convertValue(value, suit)
    unorderedList.append(trueValue)

# print(unorderedList)

#Come up with number of groups necessary
#Make lists equal to number of groups
    #Instead of above, just compare groups of two elements in a list
        #Come up with solution for odd number of elements
        #Make lists with groups of elements
        #Compare and order the groups
        #Merge the groups
        #Repeat until done
#Start combining lists in comparisons
#repeat until fully combined


list = [-3, 1, 5, 4, 2, 7, 8, 3]

def mergeSort(unorderedList):
    inputs = []
    for element in unorderedList:
        inputs.append( [element] )
    
    while len(inputs) > 1:
        inputs.append(mergeTwoLists(inputs[0], inputs[1]))
        del inputs[0]
        del inputs[0]
        
    return inputs[0]

def mergeTwoLists(inorderList1, inorderList2):
    mergedList = []
    ioList1 = 0
    ioList2 = 0
    while len(mergedList) < len(inorderList1) + len(inorderList2):
        if ioList1 >= len(inorderList1):
            mergedList += inorderList2[ioList2:]
            break
        elif ioList2 >= len(inorderList2):
            mergedList += inorderList1[ioList1:]
            break
        elif inorderList1[ioList1] < inorderList2[ioList2]:
            mergedList.append(inorderList1[ioList1])
            ioList1 += 1
        else:
            mergedList.append(inorderList2[ioList2])
            ioList2 += 1
    
    return mergedList

# print(mergeSort(list))

# startTime = time.time()

# for i in range(0, 100000):
#     sort(unorderedList)

# endTime = time.time()

#print("O(n^2) " + str(endTime - startTime))

# startTime = time.time()

# for i in range(0, 100000):
#     mergeSort(unorderedList)

# endTime = time.time()

#print("O(nlogn) " + str(endTime - startTime))

randomList = []
for i in range(0, 20000):
    randomList.append(random.randint(-10000000, 10000000))

print("made the list")

startTime = time.time()

sort(randomList)

endTime = time.time()

print("O(n^2) " + str(endTime - startTime))

startTime = time.time()

mergeSort(randomList)

endTime = time.time()

print("O(nlogn) " + str(endTime - startTime))

startTime = time.time()

randomList.sort()

endTime = time.time()

print("python " + str(endTime - startTime))