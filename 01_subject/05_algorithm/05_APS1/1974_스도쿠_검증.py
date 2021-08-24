# 스도쿠 검증
def check():                        # 검사
    for i in range(9):              # 9x9 행
        row = [0] * 10
        col = [0] * 10

        for j in range(9):          # 9x9 열
            num_row = sudoku[i][j]  # 행 검사
            num_col = sudoku[j][i]  # 열 검사
            if row[num_row]: return 0  # 중복값이 있으면 리턴 0
            if col[num_col]: return 0  # 중복값이 있으면 리턴 0

            row[num_row] = 1
            col[num_col] = 1
            # 3x3 검사도 진행
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = sudoku[r][c]
                        if square[num]: return 0
                        square[num] = 1

    return 1


T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print("#{} {}".format(tc, check()))