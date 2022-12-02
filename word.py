vowels = "aouåeiyäö"

class Word:
    def __init__(self, word):
        self.word = word
        self.stavelser = sum([word.coun(c) for c in word])

    @staticmethod
    def convert_list(li):
        return [Word(w) for w in li]

