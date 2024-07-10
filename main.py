
def printboard(xstate, zstate):
    zero='X' if xstate[0] else('o' if zstate[0] else 0)
    one='X' if xstate[1] else('o' if zstate[1] else 1)
    two='X' if xstate[2] else('o' if zstate[2] else 2)
    three='X' if xstate[3] else('o' if zstate[3] else 3)
    four='X' if xstate[4] else('o' if zstate[4] else 4)
    five='X' if xstate[5] else('o' if zstate[5] else 5)
    six='X' if xstate[6] else('o' if zstate[6] else 6)
    seven='X' if xstate[7] else('o' if zstate[7] else 7)
    eight='X' if xstate[8] else('o' if zstate[8] else 8)
    print("")
    print(f" {zero}| {one}  |  {two} ")
    print(f"---|---|---")
    print(f" {three}  | {four}  | {five}  ")
    print(f"---|---|---")
    print(f" {six}  |  {seven} |  {eight} ")
    print("")
    

def checkwin(xstate, zstate):
    wins =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if ((xstate[win[0]]+ xstate[win[1]] + xstate[win[2]]) == 3):
            print("x won the match")
            print("")
            return 1
        if ((zstate[win[0]] +  zstate[win[1]] + zstate[win[2]]) == 3):
            print("o won the match")
            print("")
            return 0
    return - 1

if __name__ =="__main__":
    xstate=[0,0,0,0,0,0,0,0,0] #for X
    zstate=[0,0,0,0,0,0,0,0,0] #for O
    turn=1 #1 for X and 0 For O
    print("welcome to Tic Tac Toe")
    while(True):
        printboard(xstate, zstate)
        if (turn==1):
            print("X's chance\n")
            value= int(input("please enter a value: "))
            xstate[value] = 1
        else:
            print("O's chance\n")
            value= int(input("please enter a value: "))
            zstate[value] = 1
        cwin = checkwin(xstate, zstate)
        if(cwin !=-1):
            print("match over")
            break
                
        turn = 1- turn

    