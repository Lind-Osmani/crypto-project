from ciphers.homophonic import HomophonicCipher
from ciphers.rail_fence import RailFenceCipher
from ciphers.morse import MorseCode

def main():
    # Create cipher objects (polymorphism in action)
    homophonic = HomophonicCipher()
    rail_fence = RailFenceCipher()
    morse = MorseCode()

    text = "HELLO WORLD"

    print("\n===== DEMO RUN =====")

    # ---------------- HOMOPHONIC ----------------
    print("\n[Homophonic Cipher]")
    enc = homophonic.encrypt(text)
    dec = homophonic.decrypt(enc)

    print("Original :", text)
    print("Encrypted:", enc)
    print("Decrypted:", dec)

    # ---------------- RAIL FENCE ----------------
    print("\n[Rail Fence Cipher]")
    enc = rail_fence.encrypt(text, 3)
    dec = rail_fence.decrypt(enc, 3)

    print("Original :", text)
    print("Encrypted:", enc)
    print("Decrypted:", dec)

    # ---------------- MORSE ----------------
    print("\n[Morse Code]")
    enc = morse.encrypt(text)
    dec = morse.decrypt(enc)

    print("Original :", text)
    print("Encrypted:", enc)
    print("Decrypted:", dec)


if __name__ == "__main__":
    main()