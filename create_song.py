import numpy as np
import random

from parse_data import get_words, get_matrix
from word import Word
import melodies


def get_next_word(current_word_vector, matrix, unique_sorted_words_words, syllables, totally_random = False):
    if totally_random:
        new_word_vector = np.matmul(matrix, current_word_vector)
    else:
        new_word_vector = np.full(len(current_word_vector), 1 / len(current_word_vector))

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

def generate_song(start_word, melody, totally_random = False):
    if start_word == "":
        return

    melody = melody[:]
        
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

    melody = None
    print("Vilken melodi vill du använda?: ")
    for i in range(len(melodies.MELODIES)):
        print(f"{i + 1}: {list(melodies.MELODIES.keys())[i]}")

    while melody is None:
        mel = input(f"Skriv i 1-{len(melodies.MELODIES)}: ")
        try:
            melody = melodies.pick_melody(int(mel) - 1)
        except ValueError:
            print("Not a number, try again")

    print(generate_song(start_word, melody))

if __name__ == "__main__":
    main()
