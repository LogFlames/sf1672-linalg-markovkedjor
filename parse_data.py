import numpy as np
from os import path


def get_words():
    words = []

    files = ["alfa.txt", "beta.txt", "epsilon.txt", "gamma.txt", "kappa.txt", "my.txt", "omikron.txt", "theta.txt", "delta.txt", "eta.txt", "_iota.txt", "lambda.txt", "ny.txt", "sigma.txt", "zeta.txt"]

    for file in files:
        with open(path.join("data", file), "r") as f:
            for line in f:
                if line.startswith("##"):
                    continue

                # Only keep the allowed characters
                cleaned_line = "".join([c for c in line.strip().lower() if c.isalpha() or c == " "])

                words.extend(cleaned_line.split())

    return words

def build_matrix(words):
    unique_sorted_words = sorted(list(set(words)))
    word_count = len(unique_sorted_words)

    print(unique_sorted_words)
    print(word_count)

    reverse_word_index_lookup = {word: i for i, word in enumerate(unique_sorted_words)}
    occurance_matrix = np.zeros((word_count, word_count))

    for keyword in unique_sorted_words:
        for i in range(len(words) - 1):
            if words[i] == keyword:
                occurance_matrix[reverse_word_index_lookup[words[i + 1]], reverse_word_index_lookup[keyword]] += 1

    prob_matrix = np.zeros((word_count, word_count))
    for col in range(word_count):
        col_sum = sum(occurance_matrix[:,col])
        if col_sum == 0:
            continue

        for row in range(word_count):
            prob_matrix[row, col] = occurance_matrix[row, col] / col_sum

    with open("probability_matrix.bin", "wb+") as f:
        np.save(f, prob_matrix)

    return prob_matrix

def get_matrix(words):
    if path.exists("probability_matrix.bin"):
        with open("probability_matrix.bin", "rb") as f:
            return np.load(f)
    else:
        return build_matrix(words)

def get_melodies():
    pass

if __name__ == "__main__":
    words = get_words()
    mat = get_matrix(words)
    print(mat)
