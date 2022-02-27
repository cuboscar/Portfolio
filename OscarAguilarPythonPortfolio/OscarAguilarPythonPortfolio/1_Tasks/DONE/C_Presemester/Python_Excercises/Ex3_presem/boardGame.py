#Author 766468
#This only provides a template for a board game. As neither rules nor winners are explained, some states are missing, but
# this basically follows the following state machine:
"""
     (3)+init_game--> switch_turn_state(1)

     (1)switch_turn_state-->verify_winner_state-->switch_turn_state(1)
                                         |
                                          -->print_results_state--> finish_playing_state(2)
     (2)finish_playing_state-->init_game(3)
                         |
                          --> terminate program (END) 


"""

def isInputAPositiveNumber(number,include0):
    try:
        val = int(number)
    except:
        print("Input is not an integer number! Try again!")
        return False
    if not include0:
        if(int(number)>0):
            return True
        else:
            print("Number must be greater than 0!")
            return False
    else: return True

#declareStates
def init_game():
    while True:
        x=input("Please enter board length (x) for the game: ")
        if(isInputAPositiveNumber(x,False)):
            x=int(x)
            break
    while True:
        y=input("Please enter board height (y) for the game: ")
        if(isInputAPositiveNumber(y,False)):
            y=int(y)
            break
    size=(x,y)
    boardI=board(size)
    gameI=game(boardI)
    print(gameI.board)
    newState="switch_turn_state"
    return ((newState,gameI))
        
def switch_turn_state(gameI):
    currentTurn=gameI.turn#Splitting turn switch and placing chip would make sense only depending on type of game
    while True:
        print("Player {}, set a{}piece.".format(currentTurn+1,gameI.pieces[currentTurn]))
        while True:
            x=input("Please provide x coordinate within the board: ")
            if(isInputAPositiveNumber(x,True)):
                if int(x)<gameI.board.x:
                    x=int(x)
                    break
        while True:
            y=input("Please provide y coordinate within the board: ")
            if(isInputAPositiveNumber(y,True)):
                if int(y)<gameI.board.y:
                    y=int(y)
                    break
        coordinate=(x,y)
        if(gameI.board.isPlaceAvailable(coordinate)):
            break
        else:
            print ("Place is occupied! Please choose somewhere else.")
    gameI.board.placePiece(gameI.pieces[currentTurn],coordinate)
    print(gameI.board)
    gameI.turnToggle()
    for i in range (len(gameI.board.board)):
        for j in range (len(gameI.board.board[i])):
            if " * " == gameI.board.board[i][j]:
                newState="switch_turn_state"
                break
            else: #in reality, verify_winner state should be called each turn to check whether or not a winner has been declared
                
                newState="verify_winner_state"
            
    print (newState)
    return ((newState,gameI))
        
#Excercise does not require a winner, therefore unused states:
def verify_winner_state(gameI):
    print("win?")
    newState="print_results_state"
    return ((newState,gameI))
        
def print_results_state(gameI):
    print("printing!")
    newState="finish_playing_state"
    return ((newState,gameI))

def finish_playing_state(gameI): #This state should ask players whether or not they'd want to continue playing
    gameI.keepPlaying=False #This output should be 'True' only if players want to continue playing
    newState=init_game
    return ((newState,gameI))
        
class board():
    """
        size-->tuple-->(int,int), (i,j)
    """
    def __init__(self,size):
        self.board=[]
        self.y=size[1]
        self.x=size[0]
        for i in range (self.y):
            buffer=[]
            for j in range (self.x):
                buffer.append(" * ")
            self.board.append(buffer)
        

    def __str__(self):
        string=" "
        for i in range(self.x):
            string+=" "+str(i)+" "
        string+="\n"
        rows=0
        string+=str(rows)
        
        for i in self.board:
            for j in i:
                string+=j
            string+="\n"
            if (self.y>rows+1):
                rows=rows+1
                string+=str(rows)
        return string
    
    def placePiece(self,piece,coordinate):
        self.board[coordinate[1]][coordinate[0]]=piece

    def isPlaceAvailable(self,coordinate):
        answer=False
        if (self.board[coordinate[1]][coordinate[0]]==" * "):
            answer=True
        return answer

class game():
    def __init__ (self,board):
        self.score=[0,0]
        self.board=board
        self.pieces=(" x "," o ")
        self.turn=0
        self.keepPlaying=True
    def turnToggle(self):
        self.turn^=1 #python toggle



if __name__=="__main__":
    print("This is ONLY a template for a game.\nAs such, this template will not have a winning condition. \nIt will end once the board is full.")
    state_game=init_game()
    state=state_game[0]
    gameI=state_game[1]
    while gameI.keepPlaying:
        state=state_game[0]
        gameI=state_game[1]
        state_game=globals()[state](gameI)
        
