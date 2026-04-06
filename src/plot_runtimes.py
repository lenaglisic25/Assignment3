import csv
import matplotlib.pyplot as plt


def main():
    files = []
    runtimes = []

    with open("results/runtimes.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            files.append(row["file"])
            runtimes.append(float(row["runtime_ms"]))

    plt.figure(figsize=(10, 6))
    plt.bar(range(len(files)), runtimes)
    plt.xticks(range(len(files)), [f.split("/")[-1] for f in files], rotation=45)
    plt.xlabel("Input File")
    plt.ylabel("Runtime (ms)")
    plt.title("HVLCS Runtime on 10 Input Files")
    plt.tight_layout()
    plt.savefig("results/runtime_graph.png")
    plt.show()


if __name__ == "__main__":
    main()