def get_znach():
    while True:
        player=input('Введіть ваш вибір ')
        if player not in sp and player!='q':
            print('Будь ласка введіть знову')
        else: 
            return player
            break



import random 
sp=["rock", "scissor", "paper"]

while True:
    player=get_znach()
    comp = random.choice(sp)
    if player=='q':break
    if player==comp:print('Drawcomputer chose ',comp)
    elif player=='rock' and comp=='scissor':print('You WIN computer chose ',comp)
    elif player=='scissor' and comp=='paper':print('You WIN computer chose ',comp)
    elif player=='paper' and comp=='rock':print('You WIN computer chose ',comp)
    else:print('You LOSE computer chose ',comp)
    