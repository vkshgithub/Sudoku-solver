# Project Completed


board=[

    [0,0,0,1,0,0,0,0,3],
    [0,0,9,0,0,5,0,0,0],
    [0,0,4,7,0,6,0,2,0],
    [0,0,0,0,0,0,0,4,0],
    [5,3,2,0,0,0,0,0,1],
    [0,0,0,0,0,1,0,6,5],
    [4,1,0,0,0,0,0,0,0],
    [0,0,0,8,4,0,6,0,0],
    [0,0,0,3,0,0,0,0,0]
]



def solve(board):
    pos=find_empty(board)
    row,col=pos
    if(row==-1 and col==-1):
        return True

    for i in range(1,10):
        if(isSafe(board,pos,i)):
            board[row][col]=i

            if(solve(board)):
                return True

            board[row][col]=0
    return False

def find_empty(board):

    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j]==0):
                return (i,j)
    return (-1,-1)

def isSafe(board,pos,num):
    row,col=pos

    for i in range(len(board)):
        if(board[row][i]==num and i!=col):
            return False

    for i in range(len(board[0])):
        if(board[i][col]==num and i!=row):
            return False


    for i in range((row // 3) * 3, ((row // 3) * 3) + 3):
        for j in range((col // 3) * 3, ((col // 3) * 3) + 3):
            if(board[i][j]==num and (i,j)!=pos):
                return False
    return True







def printfunc(board):

    for i in range(0,len(board)):
        if(i%3==0 and i!=0 and i!=len(board)-1):
            print("--------------------")

        for j in range(0,len(board[i])):
            if(j%3==0 and j!=0 and j!=len(board[i])-1):
                print("|",end="")
            print(board[i][j],end=" ")
        print(" ")

printfunc(board)
print("-------------------------------------")
solve(board)
printfunc(board)
print("-------------------")
print("rebase")
