import numpy as np
from os import path

PUNCTUATION = ".!?"
SENTENCE_CHANGE_PROBABILITY_MULTIPLIER = 0.8


def get_words():
    words = []

    files = ["alfa.txt", "beta.txt", "epsilon.txt", "gamma.txt", "kappa.txt", "my.txt", "omikron.txt", "theta.txt", "delta.txt", "eta.txt", "iota.txt", "lambda.txt", "ny.txt", "sigma.txt", "zeta.txt"]

    for file in files:
        with open(path.join("data", file), "r") as f:
            for line in f:
                if line.startswith("##"):
                    continue

                # Only keep the allowed characters
                cleaned_line = "".join([c for c in line.strip().lower() if c.isalpha() or c == " " or c in PUNCTUATION])

                words.extend(cleaned_line.split())

    unique_sorted_words = sorted(list(set(words) - {p for p in PUNCTUATION} - {"slutslutslut"}))
    return words, unique_sorted_words

def build_matrix(words, unique_sorted_words):
    word_count = len(unique_sorted_words)

    print(unique_sorted_words)
    print(word_count)

    reverse_word_index_lookup = {word: i for i, word in enumerate(unique_sorted_words)}
    occurance_matrix = np.zeros((word_count, word_count))

    for i in range(1, len(words)):
        if words[i] in PUNCTUATION or words[i] == "slutslutslut": 
            continue

        offset = -1
        mult = 1

        while words[i + offset] in PUNCTUATION:
            offset -= 1
            if i + offset < 0:
                break
            mult *= SENTENCE_CHANGE_PROBABILITY_MULTIPLIER

        if i + offset < 0:
            continue

        if words[i + offset] == "slutslutslut":
            continue

        occurance_matrix[reverse_word_index_lookup[words[i]], reverse_word_index_lookup[words[i + offset]]] += mult

    prob_matrix = np.zeros((word_count, word_count))
    for col in range(word_count):
        col_sum = sum(occurance_matrix[:,col])
        if col_sum == 0:
            continue

        prob_matrix[:,col] = occurance_matrix[:,col] / col_sum

    with open("probability_matrix.bin", "wb+") as f:
        np.save(f, prob_matrix)

    return prob_matrix


def get_matrix(words, unique_sorted_words):
    if path.exists("probability_matrix.bin"):
        with open("probability_matrix.bin", "rb") as f:
            matrix = np.load(f)
            if len(matrix) == len(set(words)):
                return matrix

    return build_matrix(words, unique_sorted_words)


if __name__ == "__main__":
    words, unique_sorted_words = get_words()
    mat = get_matrix(words, unique_sorted_words)
    print(mat)
