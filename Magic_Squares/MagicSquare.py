#  File: MagicSquare.py
#  Description: Creating a correct magic square
#  Student's Name: Pranjal Jain
#  Student's UT EID: pj5775
#  Course Name: CS 313E 
#  Unique Number: 50210
#  Date Created: 9/3/19
#  Date Last Modified: 9/6/19

#create square, implement right/down alogorithim
def make_square(n):
    #square = [[0 for x in range(n)] for y in range(n)]
    square = []

    for x in range(n):
        b = []
        for y in range(n):
            b.append(0)
        square.append(b)

    row = n - 1
    col = n//2
    
    for num in range (1, (n**2 +1)):
        square[row][col] = num
        row+= 1
        col+=1
        if row >= n:
            row = 0
        if col >= n:
            col = 0
        if square[row][col] > 0:
            row -= 2
            col -= 1
               
    return square


#print and format the square
def print_square(magic_square):
           
    for i in range(len(magic_square)):
        for j in range(len(magic_square[i])):
            print (f'{magic_square[i][j]:>4}', end='  ')
        print()


#check rows, columns, and diagnals
def check_square ( magic_square ):
    length = len(magic_square)

    #create list of all the row sums to 
    #check if each row has the same sum
    row_sums = []
    for i in range(length):
        row_sum = 0
        for j in range(length):
            row_sum += magic_square[i][j]
        row_sums.append(row_sum)

    same_row = True
    for i in range(1, len(row_sums)):
        if(row_sums[i-1] != row_sums[i]):
            same_row = False

    #create a list of all the columns sums to 
    #check if each column has the same sum
    col_sums = []
    for i in range(length):
        col_sum = 0
        for j in range(length):
            col_sum += magic_square[j][i]
        col_sums.append(col_sum)

    same_col = True
    for i in range(1, len(col_sums)):
        if(col_sums[i-1] != col_sums[i]):
            same_col = False

    #compare diagnal sums
    diag_sum = 0
    for i in range(length):
        diag_sum += magic_square[i][i]

    diag2_sum = 0
    for i in range(length):
        diag2_sum += magic_square[i][(length - 1 - i)]
        
    same_diag = True
    if diag_sum == diag2_sum:
        same_diag = True
    else:
        same_diag = False
        
    #final check to ensure all sums are the same
    if same_col == same_row == same_diag and (diag_sum == diag2_sum == row_sum == col_sum ==(length*((length**2+1)/2))):
        return True
    else:
        return False

       
def main():
    user = eval(input("Please enter an odd number: "))
    print()

    #ensures only an odd number is inputted
    while user % 2 == 0:
        user = eval(input("Please enter an odd number: "))
        print()

    sq = make_square(user)
    print('Here is a ' + str(user) + " x " + str(user) + ' magic square:\n' )
    print_square(sq)
    print()

    check = check_square(sq)
    can_sum = user*((user**2+1)//2)
    
    if check == True:
        print('This is a magic square and the canonical sum is ' + str(can_sum))
    else:
        print('This is not a magic square')
    
    
if __name__ == "__main__":
    main()

