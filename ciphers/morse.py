from .base import BaseCipher

class MorseCode(BaseCipher):

    name = "Morse"

    MORSE_DICT = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..", "9": "----."
    }

    REVERSE_DICT = {v: k for k, v in MORSE_DICT.items()}

    def encrypt(self, text):
        text = text.upper()
        return " ".join(
            "/" if c == " " else self.MORSE_DICT.get(c, "")
            for c in text
        )

    def decrypt(self, text):
        return "".join(
            " " if c == "/" else self.REVERSE_DICT.get(c, "")
            for c in text.split()
        )