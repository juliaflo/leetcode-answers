class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first attempt without looking at solutions

        # rowmap = {}
        # # check rows
        # for i in range(8):
        #     for j in range(8):
        #         if board[i][j] in rowmap.keys() and (board[i][j]).isnumeric():
        #             return False
        #         rowmap[board[i][j]] = j
        #     rowmap.clear()

        # colmap = {}
        # for i in range(8):
        #     for j in range(8):
        #         if board[j][i] in colmap.keys() and (board[j][i]).isnumeric():
        #             return False
        #         colmap[board[j][i]] = i
        #     colmap.clear()

        # sqmap = {}
        # test = map(list, zip(*board))
        # print(*test)
        # for i in board:
        #     if len(i) != (len(set(i)) + i.count(".") - 1):
        #         return False

        # return True

        # so, I ended up looking at solutions since I was literally spending hours here trying to think and test different things
        # the trail of my efforts can be seen above

        # I ended up being on the right track! Even though I wasn't able to reach any concise method
        # I was trying really hard here to avoid the "copy-paste" methods that we discussed in the last leetcode session
        # but I was having issues on how I could condense it, mostly I was stuck in sort of processing them all different ways
        # as in the rows, columns, and the 3x3 squares all differently

        # in my last attempt I had some luck in the length comparison between the list and the set! I was proud that I was able to
        # at least get on track for a more efficient way of condensing processing efforts
        # I also was trying hard to utilize dicts and lists since I know python is pretty smart with handing these data strucs

        # End of the day most solutions followed a path of saving all the numerical entries into a dict or list and condensing it
        # into a set to check length comparison since sets don't like dupes

        # make empty list to hold tuples
        entries = []

        # for every cell in the board
        for i in range(9): 
            for j in range(9):
                num = board[i][j]   # save the cell entry to a var, good practice :)

                # if the cell has a '.', don't enter it into the entries list
                # every tuple has three entries as follows:
                # (i, num) - stores the row and num of the entry
                # (num, j) - stores the num and col of the entry, swapped around so that it isn't mistaken for the row entry
                # (i // 3, j // 3, num) - stores the 3x3 that the num is in by finding the floor div of the row and col and the num
                if num != '.':
                    entries += ((i, num), (num, j), (i // 3, j // 3, num))  # if it isn't, add it
                
        # return the result of comparing lengths, returns true if theyre the same and false if not
        return len(entries) == len(set(entries))