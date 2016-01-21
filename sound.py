import winsound
import random

#winsound.PlaySound('F:\Python3Game-master\sounds\sound effects\enemy shout.wav',winsound.SND_NOSTOP) # for testing

if enemy1l_explosion == true or enemy1r_explosion == true:
    winsound.PlaySound('F:\Python3Game-master\sounds\sound effects\explosion.wav',winsound.SND_NOSTOP)

if death == True:
    randsound = random.randint (0, 6)
    print(randsound)
    if randsound == 0:
        winsound.PlaySound("F:\Python3Game-master\sounds\trump quotes\Donald Trump - Part of the beauty of me is that I'm very rich.wav",winsound.SND_NOSTOP)
    elif randsound == 1:
        winsound.PlaySound("F:\Python3Game-master\sounds\trump quotes\Donald Trump got a SMALL loan of 1 million dollars.wav",winsound.SND_NOSTOP)
    elif randsound == 2:
        winsound.PlaySound("F:\Python3Game-master\sounds\trump quotes\Donald Trump- I Have A Great Relationship With The Blacks.wav",winsound.SND_NOSTOP)
    elif randsound == 3:
        winsound.PlaySound("F:\Python3Game-master\sounds\trump quotes\Donald Trump- I'm Rich!.wav",winsound.SND_NOSTOP)
    elif randsound == 4:
        winsound.PlaySound("F:\Python3Game-master\sounds\trump quotes\Donald Trump- Mexicans are rapists.wav",winsound.SND_NOSTOP)
    elif randsound == 5:
        winsound.PlaySound("F:\Python3Game-master\sounds\trump quotes\Donald Trump- 'Somebody's doing the raping'.wav",winsound.SND_NOSTOP)
    elif randsound == 6:
        winsound.PlaySound("F:\Python3Game-master\sounds\trump quotes\Nobody would be tougher on ISIS than Donald Trump.wav",winsound.SND_NOSTOP)
