rom ciphers.homophonic import HomophonicCipher
from ciphers.rail_fence import RailFenceCipher
from ciphers.morse import MorseCode


def main():
    # Registry (Strategy Pattern)
    ciphers = {
        "1": HomophonicCipher(),
        "2": RailFenceCipher(),
        "3": MorseCode()
    }

    while True:
        print("\n========== CIPHER SYSTEM ==========")

        for key, cipher in ciphers.items():
            print(f"{key}. {cipher.name}")

        print("0. Exit")

        choice = input("Zgjedh opsionin: ")

        if choice == "0":
            print("Programi u mbyll.")
            break

        cipher = ciphers.get(choice)

        if cipher:
            cipher.run()   # 🔥 polymorphism in action
        else:
            print("Opsion i pavlefshëm!")


if __name__ == "__main__":
    main()