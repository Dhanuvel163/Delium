# SETTING VARIABLES
limits = {
    'HITTINGLIMIT': 2,
    'INITIALLIMIT': 2
}
values = {
    'A': 1, 'K': 10, 'J': 10, 'Q': 10, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
}
actions = {
    'HIT': 'HIT',
    'STAY': 'STAY',
    'DONE': 'DONE'
}
# listValues = ['A', 'K', 'J', 'Q']


def calculateSum(listOfValues):
    print(listOfValues)
    sum = 0
    for i in listOfValues:
        sum += values[i]
    return sum


def checkHits(hitsDict):
    status = False
    for i in hitsDict.values():
        if(i != 2):
            status = True
    return status


def StartGame():
    gamedict = {}
    hitsDict = {}
    Gameover = False

    # INITIAL STAGE SETTING UP
    print('Initial Stage :')
    for i in range(n):
        print('Player', i+1, ': ', end="")
        tempInitial = [i for i in input().split(" ")]
        gamedict[i] = tempInitial
        hitsDict[i] = 0

    # GAME START
    while Gameover == False:
        for i in range(n):
            print('Player ', (i+1), '(HIT/STAY) : ', end="")
            action = input()

            if(action == actions['STAY']):
                pass
            elif (action == actions['HIT']):
                hitsDict[i] += 1
                print('Player ', (i+1), ' : ', end="")
                cardGot = input()
                gamedict[i].append(cardGot)
            elif(action == actions['DONE']):
                Gameover = True
                break
            status = checkHits(hitsDict)
            if status == False:
                Gameover = True
                break

    # PREDICTING WINNER
    winner = 0
    winnervalue = 0
    for i in range(n):
        data = calculateSum(gamedict[i])
        if(data > winnervalue and data <= 21):
            winner = i
            winnervalue = data

    print('Winner is Player ', (int(winner)+1), '')


n = int(input('Enter Number of Players : '))
StartGame()
