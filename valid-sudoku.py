class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        columns = [0] * 9
        squares = [[0] * 3 for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                number = int(board[i][j])
                bit_representation_of_number = 1 << (number - 1)
                if bit_representation_of_number & rows[i]:
                    return False
                if bit_representation_of_number & columns[j]:
                    return False
                if bit_representation_of_number & squares[i // 3][j // 3]:
                    return False

                rows[i] |= bit_representation_of_number
                columns[j] |= bit_representation_of_number
                squares[i // 3][j // 3] |= bit_representation_of_number

        return True
