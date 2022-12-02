vowels = "aouåeiyäö"

class Word:
    def __init__(self, word):
        self.word = word
        self.syllables = Word.count_syllables(word)

    @staticmethod
    def convert_list(li):
        return [Word(w) for w in li]

    @staticmethod
    def count_syllables(word):
        return sum([word.count(vowel) for vowel in vowels])

