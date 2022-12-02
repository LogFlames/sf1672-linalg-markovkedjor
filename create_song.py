import numpy as np
from parse_data import get_words, get_matrix
from word import Word


def get_next_word(current_word_vector, matrix, unique_sorted_words_words, syllables):
    new_word_vector = np.matmul(matrix, current_word_vector)

    for i in range(len(new_word_vector)):
        if unique_sorted_words_words[i].syllables > syllables:
            div = unique_sorted_words_words[i].syllables - syllables + 1

            new_word_vector[i] /= div

    norm = sum(new_word_vector)
    if norm != 0:
        new_word_vector = new_word_vector / norm

    new_word_index = np.random.choice(
        range(len(new_word_vector)), 1, p=new_word_vector)[0]

    return new_word_index

def generate_song(start_word, melody):
    if start_word == "":
        return
        
    words = get_words()

    unique_sorted_words = sorted(list(set(words)))
    unique_sorted_words_words = Word.convert_list(unique_sorted_words)

    probability_matrix = get_matrix(words)

    current_word_vector = np.zeros(len(unique_sorted_words))
    current_word_vector[unique_sorted_words.index(start_word)] = 1

    song = start_word + " "
    melody[0] -= Word.count_syllables(start_word)

    line = 0
    while True:
        next_word_index = get_next_word(
            current_word_vector, probability_matrix, unique_sorted_words_words, melody[line])

        song += unique_sorted_words[next_word_index] + " "
        melody[line] -= unique_sorted_words_words[next_word_index].syllables
        while line < len(melody) and melody[line] <= 0:
            song += "\n"
            line += 1

        if line >= len(melody):
            break

        current_word_vector = np.zeros(len(unique_sorted_words))
        current_word_vector[next_word_index] = 1

    return song

def main():
    words = get_words()

    unique_sorted_words = sorted(list(set(words)))

    while (start_word := input("What word do you want to start the song on?: ").lower()) not in unique_sorted_words:
        print(f"The word '{start_word}' does not occur in the dataset, please try again.")

    print(generate_song(start_word, [9, 11, 9, 9, 0, 11, 11, 9, 9, 9, 2]))


if __name__ == "__main__":
    main()
