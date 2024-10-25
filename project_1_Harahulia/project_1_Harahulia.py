from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"""+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+\n""")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    free_fields = make_list_of_free_fields(board) #викликаємо список вільних клітин
    while True:
        player_move = int(input("Enter your move: "))
        if player_move < 1 or player_move > 9: #Перевіряємо чи введена клітина існує
            print("Wrong cell value. Try again.")
        else:
            if (player_move < 4) and (0, player_move - 1) in free_fields: #якщо клітина лежить в першому рядку
                board[0][player_move - 1] = 'O'
                break
            elif (3 < player_move < 7) and (1, player_move - 4) in free_fields: #якщо клітина лежить в другому рядку
                board[1][player_move - 4] = 'O'
                break
            elif (player_move > 6) and (2, player_move - 7) in free_fields:#якщо клітина лежить в третьому рядку
                board[2][player_move - 7] = 'O'
                break
            else: print("Cell is already occupied. Try again.")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] != 'O') and (board[i][j] != 'X'):
                free_squares.append((i, j))
    return free_squares

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    sign1 = None
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2]\
            or board[0][i] == board[1][i] == board[2][i]:   #перевірка рядів і стовпців на перемогу
            sign1 = board[i][i]                             #запам'ятовуємо Хто виграв
        elif board[0][0] == board[1][1] == board[2][2]\
            or board[0][2] == board[1][1] == board[2][0]:   #перевірка діагоналей на перемогу
            sign1 = board[1][1]                             #запам'ятовуємо Хто виграв
    if sign1 == sign:
        return True

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)

    if ((1, 1)) in free_fields:     #перший крок за комп'ютером -- центр
        board[1][1] = 'X'
    else:
        move = free_fields[randrange(len(free_fields))] #вибирає "випадкову" клітину з вільних
        board[move[0]][move[1]] = 'X'
    if len(free_fields) == 1: return True               #якщо це хід в останню вільну -- час завершувати
    return False



board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

while True:
    is_the_last = draw_move(board)
    display_board(board)
    if is_the_last:
        print("Where is no winner")
        break
    if victory_for(board, 'X'):
        print("Computer won!")
        break
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You won!")
        break
