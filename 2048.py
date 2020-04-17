import random

"""Generating initial conditions"""
def initials():
    """generating initial numbers"""
    a=2**random.randint(1,2)
    matrix[random.randint(0,order-1)][random.randint(0,order-1)]=2
    while (True):
        x=random.randint(0,order-1)
        y=random.randint(0,order-1)
        if matrix[x][y]==0:
            matrix[x][y]=a
            break

def printing():
    """Printing the matrix"""
    for i in range(order):
        print matrix[i]


"""for generating a number at each step"""
def generate():
    while(True):
        if matrix[random.randint(0,order-1)][random.randint(0,order-1)]==0:
            matrix[random.randint(0,order-1)][random.randint(0,order-1)]=2**random.randint(1,2)
            break



"""Taking keyboard input from user"""
def swipe():
    print "\n\nEnter....\n'w' to swipe up\n's' to swipe down\n'a' to swipe left\n'd' to swipe right\n"
    swipe_value=raw_input()
    if swipe_value =='W' or swipe_value=='w':
        up_swipe()
    elif swipe_value =='S' or swipe_value=='s':
        down_swipe()
    elif swipe_value =='A' or swipe_value=='a':
        left_swipe()
    elif swipe_value =='D' or swipe_value=='d':
        right_swipe()
    else:
        print "\nPlease enter a valid choice!\n\n"




"""Up swipe function"""   
def up_swipe():
    global score
    for c in range(order):
        for traverse in range(order-1):
            for r in range(order-traverse-1):
                if matrix[r][c]==0 and matrix[r+1][c]!=0:
                    matrix[r+1][c],matrix[r][c]=matrix[r][c],matrix[r+1][c]
    for c in range(order):
        for r in range(order-1):
            if matrix[r][c]==matrix[r+1][c] and matrix[r+1][c]!=0:
                matrix[r][c]=matrix[r][c]+matrix[r+1][c]
                matrix[r+1][c]=0
                score=score+matrix[r][c]
    print "\nScore"
    print score
    print "\n"
    generate()
    printing()



"""Down swipe function"""
def down_swipe():
    global score
    for c in range(order):
        for traverse in range(order,1,-1):
            for r in range(order-1,order-traverse-1,-1):
                if matrix[c][r]==0 and matrix[c-1][r]!=0:
                    matrix[c-1][r],matrix[c][r]=matrix[c][r],matrix[c-1][r]
    for c in range(order):
        for r in range(order-1,1,-1):
            if matrix[c][r]==matrix[c-1][r] and matrix[c-1][r]!=0:
                matrix[c][r]=matrix[c][r]+matrix[c-1][r]
                matrix[c-1][r]=0
                score=score+matrix[c][r]
    print "\nScore"
    print score
    print "\n"
    generate()
    printing()



"""Left swipe function"""
def left_swipe():
    global score
    for c in range(order):
        for traverse in range(order-1):
            for r in range(order-traverse-1):
                if matrix[c][r]==0 and matrix[c][r+1]!=0:
                    matrix[c][r+1],matrix[c][r]=matrix[c][r],matrix[c][r+1]
    for c in range(order):
        for r in range(order-1):
            if matrix[c][r]==matrix[c][r+1] and matrix[c][r+1]!=0:
                matrix[c][r]=matrix[c][r]+matrix[c][r+1]
                matrix[c][r+1]=0
                score=score+matrix[c][r]
    print "\nScore"
    print score
    print "\n"        
    generate()
    printing()



"""Right swipe function"""
def right_swipe():
    global score
    for c in range(order):
        for traverse in range(order,1,-1):
            for r in range(order-1,order-traverse-1,-1):
                if matrix[r][c]==0 and matrix[r][c-1]!=0:
                    matrix[r][c-1],matrix[r][c]=matrix[r][c],matrix[r][c-1]
    for c in range(order):
        for r in range(order-1,1,-1):
            if matrix[r][c]==matrix[r][c-1] and matrix[r][c-1]!=0:
                matrix[r][c]=matrix[r][c]+matrix[r][c-1]
                matrix[r][c-1]=0
                score=score+matrix[r][c]
    print "\nScore"
    print score
    print "\n"
    generate()
    printing()




"""_____________main_______________"""


    
score=0

"""Creating the matrix"""
order=int(input("Enter the matrix size from 3 to 8: "))

while not(order>=3 and order<=8):
    order=int(input("\nWrong Input!!\n\nEnter the matrix size from 3 to 8: "))
matrix=[[0 for column in range(order)] for row in range(order)]
    
initials()
while True:
    print "____________________________________________"
    printing()
    swipe()
