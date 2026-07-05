
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            temp_set = set({})
            print(i)
            for j in i:
                if j == '.' or j not in temp_set:
                    if j != '.':
                        temp_set.add(j)
                        
                    continue
                else:
                    print("1st check")
                    return False
        for i in range(0,9):
            temp_set = set({})
            for j in range(0,9):
                if board[j][i] == '.' or board[j][i] not in temp_set:
                    if board[j][i] != '.':
                        temp_set.add(board[j][i])
                    continue
                else:
                    print("2nd check")
                    return False
        for t in range(3):
            for p in range(3):
                temp_list = []
                for k in range(t*3,t*3+3):
                    for l in range(p*3,p*3+3):
                        temp_list.append(board[k][l])
                print(temp_list)
                temp_set = set({})
                for j in temp_list:
                    if j == '.' or j not in temp_set:
                        if j != '.':
                            temp_set.add(j)           
                        continue
                    else:
                        print("3rd check")
                        return False
        return True


