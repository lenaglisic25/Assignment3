cat > src/runtime_test.py <<'PY'
import sys
import time
import csv
from pathlib import Path
from hvlcs import compute_hvlcs


def read_file(path):
    with open(path, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip() != ""]

    k = int(lines[0])
    values = {}

    for i in range(1, k + 1):
        ch, val = lines[i].split()
        values[ch] = int(val)

    a = lines[k + 1]
    b = lines[k + 2]
    return values, a, b


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 src/runtime_test.py data/test1.in data/test2.in ...")
        sys.exit(1)

    rows = []

    for filename in sys.argv[1:]:
        values, a, b = read_file(filename)

        start = time.perf_counter()
        compute_hvlcs(values, a, b)
        end = time.perf_counter()

        runtime_ms = (end - start) * 1000.0
        rows.append([filename, len(a), len(b), runtime_ms])

    Path("results").mkdir(exist_ok=True)

    with open("results/runtimes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["file", "len_a", "len_b", "runtime_ms"])
        writer.writerows(rows)

    print("Saved results to results/runtimes.csv")


if __name__ == "__main__":
    main()
PY