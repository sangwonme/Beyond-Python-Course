import sys

def get_mismatch_count(grid, N):
    """Calculate the number of operations needed to restore symmetry."""
    mismatch_count = 0
    half_N = N // 2
    for i in range(half_N):
        for j in range(half_N, N):
            mirror_i = N - 1 - i
            mirror_j = N - 1 - j
            
            top_right = grid[i][j]
            bottom_right = grid[mirror_i][j]
            top_left = grid[i][mirror_j]
            bottom_left = grid[mirror_i][mirror_j]
            
            values = {top_right, top_left, bottom_right, bottom_left}
            mismatch_count += len(values) - 1
    return mismatch_count

# Read input
N, U = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(N)]

# Calculate initial mismatches
mismatch_count = get_mismatch_count(grid, N)
print(mismatch_count)

# Process updates
for _ in range(U):
    r, c = map(int, sys.stdin.readline().split())
    r -= 1
    c -= 1
    
    # Toggle the cell
    grid[r][c] = '#' if grid[r][c] == '.' else '.'
    
    # Recalculate mismatch count
    mismatch_count = get_mismatch_count(grid, N)
    print(mismatch_count)
