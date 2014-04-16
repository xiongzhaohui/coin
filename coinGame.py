import random
f = open("score.txt","r+")
score=f.read()
highscore = int(score)
print "Coin Guessing game. All time high score:", highscore, "correct"
userscore=0
while True:
    guess = raw_input("please predict heads or tails")
    coin = random.randint(0,1)
    if guess == "heads" and coin == 0:
        userscore = userscore + 1
        print "It is heads,", "you score is:", userscore
    if guess == "tails" and coin == 1:
        userscore = userscore + 1
        print " It is tails", " you score is:", usersocre
    if guess == "heads" and coin == 1:
        print "It is tails, Game over"
        break
    if guess == "tails" and coin == 0:
        print "It is heads, game over."
        break
if highscore < userscore:
    highscore = userscore
print "you score:", userscore
f.seek(0)
f.truncate()
f.write(str(highscore))

