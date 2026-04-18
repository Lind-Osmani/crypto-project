from .base import BaseCipher

class RailFenceCipher(BaseCipher):
    def __init__(self):
        super().__init__("Rail Fence Cipher")

    def encrypt(self, text: str, rails: int) -> str:
        if rails == 1:
            return text
        
        fence = [[] for _ in range(rails)]
        row, direction = 0, 1

        for char in text:
            fence[row].append(char)

            row += direction

            if row == 0 or row == rails - 1:
                direction *= -1

        return "".join("".join(r) for r in fence)
    
    def decrypt(self, text: str, rails: int) -> str:
        if rails == 1: 
            return text
        
        pattern = [[] for _ in range(rails)]
        row, direction = 0, 1

        for _ in text:
            pattern[row].append("*")
            row += direction

            if row == 0 or row == rails - 1:
                direction *= -1

        index = 0
        for i in range(rails):
            for j in range(len(pattern[i])):
                pattern[i][j] = text[index]
                index += 1

        result = []
        row, direction = 0, 1
        pointers = [0] * rails

        for _ in text:
            result.append(pattern[row][pointers[row]])
            pointers[row] += 1

            row += direction

            if row == 0 or row == rails - 1:
                direction *= -1

        return "".join(result)