from abc import ABC, abstractmethod

class BaseCipher(ABC):
    """
    Abstract base class for all ciphers.
    Demonstrates POLYMORPHISM.
    """
    
    @abstractmethod
    def encrypt(self, text):
        pass

    @abstractmethod
    def decrypt(self, text):
        pass
        
    def run(self):
        text = input("Shkruaj tekstin: ")

        encrypted = self.encrypt(text)
        decrypted = self.decrypt(encrypted)

        print("Original :", text)
        print("Encrypted:", encrypted)
        print("Decrypted:", decrypted)