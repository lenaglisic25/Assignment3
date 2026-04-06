import sys


def read_input():
    data = sys.stdin.read().split()

    k = int(data[0])
    values = {}

    index = 1
    for _ in range(k):
        char = data[index]
        value = int(data[index + 1])
        values[char] = value
        index += 2

    a = data[index]
    b = data[index + 1]

    return values, a, b


def compute_hvlcs(values, a, b):
    n = len(a)
    m = len(b)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                take = dp[i - 1][j - 1] + values[a[i - 1]]
                skip_a = dp[i - 1][j]
                skip_b = dp[i][j - 1]
                dp[i][j] = max(take, skip_a, skip_b)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = n
    j = m
    result = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1] and dp[i][j] == dp[i - 1][j - 1] + values[a[i - 1]]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return dp[n][m], "".join(result)


def main():
    values, a, b = read_input()
    best_value, subsequence = compute_hvlcs(values, a, b)
    print(best_value)
    print(subsequence)


if __name__ == "__main__":
    main()