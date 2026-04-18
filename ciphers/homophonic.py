import random
import string
from .base import BaseCipher

class HomophonicCipher(BaseCipher):

    def __init__(self):
        self.alphabet = string.ascii_uppercase
        self.mapping = {}
        self.reverse_mapping = {}

        pool = list(range(10, 99))
        random.shuffle(pool)

        for letter in self.alphabet:
            codes = [str(pool.pop()) for _ in range(3)]
            self.mapping[letter] = codes

            for c in codes:
                self.reverse_mapping[c] = letter

    def encrypt(self, text):
        text = text.upper()
        result = []

        for char in text:
            if char in self.mapping:
                result.append(random.choice(self.mapping[char]))
            else:
                result.append(char)

        return " ".join(result)

    def decrypt(self, text):
        return "".join(self.reverse_mapping.get(c, c) for c in text.split())