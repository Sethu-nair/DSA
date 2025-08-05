class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]    #[.Q..,...Q,Q...,..Q.]
        board=[]     #[1,3,0,2]

        cols=set()     #which col already has queens
        diag1=set()    #(row-col) tracks ↘
        diag2=set()    #(row+col) tracks ↙  check if they are on same diagonals 

        def backtrack(row):
            if row==n:
                temp=[]  # convert number to row eg:   i = 1 → .Q..    i = 3 → ...Q later result add
                for i in board:
                    line="."*i+"Q"+"."*(n-i-1)
                    temp.append(line)
                result.append(temp)
                return

            for col in range(n):            #try every column in this row
                if col in cols or (row-col)in diag1 or (row+col) in diag2:    #if place in same col or diag,skip
                    continue
                board.append(col)
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)

                backtrack(row+1)   #try placing the queen on the next row

                board.pop()       #backtrack steps
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)   

        backtrack(0)      #try the step again from 0
        return result



