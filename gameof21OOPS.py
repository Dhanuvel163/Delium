class GAME:
    def __init__(self, number):
        self.limits = {
            'HITTINGLIMIT': 2,
            'INITIALLIMIT': 2
        }
        self.actions = {
            'HIT': 'HIT',
            'STAY': 'STAY',
            'DONE': 'DONE'
        }
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
            if(self.players[i].getHitcount() != 2):
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


class PLAYER:

    def __init__(self, initial):
        self.values = {
            'A': 1, 'K': 10, 'J': 10, 'Q': 10, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }
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


n = int(input('Enter Number of Players : '))
newgame = GAME(n)
newgame.StartGame()
