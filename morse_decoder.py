from morse_tree import MorseTree
def main():
    morse = MorseTree()

    morse.add("A", ".-")
    morse.add("B", "-...")

    print(morse)
if __name__ == "__main__":
    main()