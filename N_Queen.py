def solve_nqueens(n):
    placement = [-1] * n
    solve(placement, 0, n)

def solve(placement, row, n):
    if row == n:
        print_solution(placement)
        return

    for i in range(n):
        if is_valid(placement, row, i):
            placement[row] = i
            solve(placement, row + 1, n)

def is_valid(placement, row, col):
    for i in range(row):
        if placement[i] == col or abs(placement[i] - col) == abs(i - row):
            return False
    return True

def print_solution(placement):
    n = len(placement)
    for i in range(n):
        for j in range(n):
            if placement[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# Example usage with N = 8
solve_nqueens(8)