import numpy as np
from os import path


allowed_chars = "abcdefghijklmnopqrstuvwxyzåäö "

def read_data():
    words = set()

    files = ["alfa.txt", "beta.txt"]

    for file in files:
        with open(path.join("data", file), "r") as f:
            for line in f:
                # Ignore lines with titles and melodies
                if line.startswith("##"):
                    continue

                # Only keep the allowed characters
                cleaned_line = "".join([c for c in line.strip().lower() if c in allowed_chars])

                words |= set(cleaned_line.split())

            f.read().lower()

    return data

if __name__ == "__main__":
    data = read_data()
