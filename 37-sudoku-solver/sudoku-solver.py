class Solution:
    def solveSudoku(self, board):
        # Keep track of used numbers in rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Step 1: Preprocess the board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)
                else:
                    empty_cells.append((r, c))

        def backtrack(index):
            # If we've filled all empty cells, we're done
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            box_id = (r // 3) * 3 + (c // 3)

            for digit in '123456789':
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[box_id]:
                    # Place the digit
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_id].add(digit)

                    if backtrack(index + 1):
                        return True  # success

                    # Backtrack
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_id].remove(digit)

            return False  # No digit fits here

        backtrack(0)
