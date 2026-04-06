cat > src/hvlcs.py <<'PY'
import sys


def read_input():
    lines = [line.rstrip("\n") for line in sys.stdin if line.strip() != ""]
    if not lines:
        return {}, "", ""

    k = int(lines[0])
    values = {}

    for i in range(1, k + 1):
        parts = lines[i].split()
        ch = parts[0]
        val = int(parts[1])
        values[ch] = val

    a = lines[k + 1]
    b = lines[k + 2]

    return values, a, b


def compute_hvlcs(values, a, b):
    n = len(a)
    m = len(b)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if a[i] == b[j]:
                take = values[a[i]] + dp[i + 1][j + 1]
                skip_a = dp[i + 1][j]
                skip_b = dp[i][j + 1]
                dp[i][j] = max(take, skip_a, skip_b)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    subseq = reconstruct(values, a, b, dp)
    return dp[0][0], subseq


def reconstruct(values, a, b, dp):
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            take = values[a[i]] + dp[i + 1][j + 1]
            if dp[i][j] == take:
                result.append(a[i])
                i += 1
                j += 1
                continue

        if dp[i][j] == dp[i + 1][j]:
            i += 1
        else:
            j += 1

    return "".join(result)


def main():
    values, a, b = read_input()
    best_value, subseq = compute_hvlcs(values, a, b)
    print(best_value)
    print(subseq)


if __name__ == "__main__":
    main()
PY