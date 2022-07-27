import random
import sys
import os


def main():
    file = sys.argv[1]
    randomize_text_lines(file)


def randomize_text_lines(file):
    num = 0
    with open(file, "r") as f:
        results = [line.strip() for line in f]
    random.shuffle(results)
    filename, ext = os.path.splitext(file)
    filename_shuffled = filename + "-SHUFFLED"
    filename_shuffled2 = filename + "-SHUFFLED"
    while os.path.exists(f"{filename_shuffled}{ext}"):
        num += 1
        filename_shuffled = f"{filename_shuffled2}" + str(num)
    with open(f"{filename_shuffled}{ext}", "x") as f:
        for i in results:
            f.write(i + "\n")
    return "done"


if __name__ == "__main__":
    main()