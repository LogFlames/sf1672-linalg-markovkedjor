import numpy as np
from parse_data import get_words, get_matrix


def get_next_word(current_word_vector, matrix):
    new_word_vector = np.matmul(matrix, current_word_vector)
    new_word_index = np.random.choice(
        range(len(new_word_vector)), 1, p=new_word_vector)[0]

    return new_word_index

def generate_song(start_word, melody):
    words = get_words()

    unique_sorted_words = sorted(list(set(words)))

    probability_matrix = get_matrix(words)

    current_word_vector = np.zeros(len(unique_sorted_words))
    current_word_vector[unique_sorted_words.index(start_word)] = 1

    song = start_word + " "

    while True:
        next_word_index = get_next_word(
            current_word_vector, probability_matrix)

        if unique_sorted_words[next_word_index] == "slutslutslut":
            break

        song += unique_sorted_words[next_word_index] + " "

        current_word_vector = np.zeros(len(unique_sorted_words))
        current_word_vector[next_word_index] = 1

    return song

def main():
    words = get_words()

    unique_sorted_words = sorted(list(set(words)))

    while (start_word := input("What word do you want to start the song on?: ").lower()) not in unique_sorted_words:
        print(f"The word '{start_word}' does not occur in the dataset, please try again.")

    print(generate_song(start_word, None))


if __name__ == "__main__":
    main()
