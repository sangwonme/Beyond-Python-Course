def count_stars_before_shift(t, test_cases):
    results = []

    for case in test_cases:
        n, a, b, grid = case
        stars = set()

        # Process the grid
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 'B':
                    # Black pixel, must overlap in both photos
                    stars.add((i, j))

        # Check if the configuration is valid
        valid = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 'G':
                    # Gray pixel, exists in exactly one photo
                    # We need to check if this position could have been reached by a star
                    if not ((i - b, j - a) in stars or (i, j) in stars):
                        valid = False
                        break

            if not valid:
                break

        if valid:
            results.append(len(stars))
        else:
            results.append(-1)

    return results

# Input reading and parsing
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    test_cases = []
    index = 1

    for _ in range(T):
        n, a, b = map(int, data[index].split())
        index += 1
        grid = [data[index + i] for i in range(n)]
        index += n
        test_cases.append((n, a, b, grid))

    results = count_stars_before_shift(T, test_cases)

    # Print results
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
