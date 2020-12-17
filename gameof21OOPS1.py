class GAME:
    def __init__(self, number):
        self.limits = {'HITTINGLIMIT': setlimits.getHittingLimit(
        ), 'INITIALLIMIT': setlimits.getInitialLimit()}
        self.actions = {'HIT': 'HIT', 'STAY': 'STAY', 'DONE': 'DONE'}
        self.Noofplayers = number
        self.players = {}
        print('Initial Stage :')
        for i in range(number):
            print('Player', i+1, ': ', end="")
            tempInitial = [i for i in input().split(" ")]
            tempPlayer = PLAYER(tempInitial)
            self.players[i] = tempPlayer

    def predictWinner(self):
        winner = 0
        winnervalue = 0
        for i in range(self.Noofplayers):
            data = self.players[i].getScore()
            if(data > winnervalue and data <= 21):
                winner = i
                winnervalue = data
        print('Winner is Player ', (int(winner)+1), '')

    def checkHits(self):
        status = False
        for i in range(self.Noofplayers):
            if(self.players[i].getHitcount() != self.limits['HITTINGLIMIT']):
                status = True
        return status

    def StartGame(self):
        Gameover = False
        # GAME START
        while Gameover == False:
            for i in range(self.Noofplayers):
                print('Player ', (i+1), '(HIT/STAY/DONE) : ', end="")
                action = input()
                if(action == self.actions['STAY']):
                    pass
                elif (action == self.actions['HIT']):
                    print('Player ', (i+1), ' : ', end="")
                    cardGot = input()
                    self.players[i].hit(cardGot)
                elif(action == self.actions['DONE']):
                    Gameover = True
                    break
                status = self.checkHits()
                if status == False:
                    Gameover = True
                    break

        # PREDICTING WINNER
        self.predictWinner()


class VALUES:
    def __init__(self):
        self.values = {
            'A': 1, 'K': 10, 'J': 10, 'Q': 10, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }

    def add(self, key, value):
        self.values[key] = value

    def get(self):
        return self.values


class LIMITS:
    def __init__(self):
        self.limits = {
            'HITTINGLIMIT': 2,
            'INITIALLIMIT': 2
        }

    def setInitialLimit(self, value):
        self.limits['INITIALLIMIT'] = value

    def setHittingLimit(self, value):
        self.limits['HITTINGLIMIT'] = value

    def getInitialLimit(self):
        return self.limits['INITIALLIMIT']

    def getHittingLimit(self):
        return self.limits['HITTINGLIMIT']


class PLAYER:
    def __init__(self, initial):
        self.values = setvalues.get()
        self.cardsList = initial
        self.scores = 0
        for j in initial:
            self.scores += self.values[j]
        self.hitcount = 0

    def hit(self, card):
        self.cardsList.append(card)
        self.scores += self.values[card]
        self.hitcount += 1

    def getHitcount(self):
        return self.hitcount

    def getScore(self):
        return self.scores


# Setting Values Of Cards
setvalues = VALUES()
print("Do You Want to Add values to cards ? (YES/NO) : ", end="")
answer = input()
while answer == 'YES':
    key, val = input('Enter the card:value  : ').split(":")
    setvalues.add(key, val)
    print("Do You Want to Add more values to cards ? (YES/NO) : ", end="")
    answer = input()

# Setting Limits
setlimits = LIMITS()
print("Do You Want to set limits ? (YES/NO) : ", end="")
ans = input()
if(ans == 'YES'):
    hitlimit = int(input('Enter the hitting limit : '))
    setlimits.setHittingLimit(hitlimit)
    initiallimit = int(input('Enter the initial limit : '))
    setlimits.setInitialLimit(initiallimit)

# Start Cards
while True:
    print("\n------------------------Game Started-------------------------")
    n = int(input('Enter Number of Players : '))
    newgame = GAME(n)
    newgame.StartGame()
