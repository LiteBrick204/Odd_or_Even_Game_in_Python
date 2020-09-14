#!/usr/bin/env python
import random
def toss(u):
    t = random.randint(0,1)
    g = "bat" if bool(t) else "bowl"
    if u==t:
        return [int(input("You Won the Toss! Press 1 to bat and 2 to bowl:")),u==g]
    else:
        print("Computer won the toss and choose to",g)
        return [t+1,u==g]

def check(C,w):
    if C=='n':
        if not w:print("Thank you for playing")
        quit()
    elif C=='y' and w:
        game()

class GameOver(Exception):
    pass

def game():
    score = 0
    C = input("Do you want to start(Y/N):")
    check(C,0)
    l = int(input("Call for toss! Press 0 for head and 1 for tail :"))
    B = toss(l)
    f = 1
    c,u = 0,3
    while c!=u and f==1 and C=='y':
        try:
            g = random.randint(1,6)
            u = int(input(">>>"))
            print("Computer Entered",g)
            if u<=0 or u>6:
                f = 2
                raise ValueError
            if u==g and B[0]==1:
                print("YOU ARE OUT!!")
                print("Your Score is",score)
                f = -1
                raise GameOver
            elif u==g and B[0]==2:
                print("The Computer is out!")
                batround(score+1,1)
            else:
                score+=u if B[0]==1 and B[1] else g
                continue

        except GameOver:
            if f==-1:
                batround(score+1,0)
        except ValueError:
            if f==-1:
                print("You can only enter numbers between 1-6 only")
                u=0
                f=0
            continue

def batround(N,who):
    print("%s need"%("You" if who else "Computer"),N,"runs to win the match!!")
    u,c,f = 1,3,0
    while N:
        try:
            g = random.randint(1,6)
            u = int(input(">>>"))
            print("Computer Entered",g)
            if u<=0 or u>6:
                f = 2
                raise ValueError
            elif u==g:
                print("%s ARE OUT!!"%("You" if who else "Computer"))
                print("Remaining Score is",N)
                f = -1
                raise GameOver
            elif ((who and (N-u)<=0) or (not who and (N-g)<=0)) or N==0:
                print("%s won the match!!" %("You" if who else "Computer"))
                raise GameOver
            elif (who and u in range(1,7)): N-=u
            elif not who: N-=g
        except ValueError:
            if f==2:
                print("You can only enter numbers between 1-6 only")
                u=0
                f=0
        except GameOver:
            print("GG!! Thank You for Playing with me.\nKudos and Godspeed!!!\n\t\t\t~Computer")
            check(input("Enter n to quit: ").strip(),1)
game()
