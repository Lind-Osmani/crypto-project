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