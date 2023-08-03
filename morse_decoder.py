from morse_tree import MorseTree
def main():
    morse = MorseTree()

    morse.add("A", ".-")
    morse.add("B", "-...")
    morse.add("C", "-.-.")
    morse.add("D", "-..")
    morse.add("E", ".")

    morse.add("T", "-")


    # TODO load all characters from the file on Canvas

    # TODO take string input from user to decode (or load from file).

    # what we can't do yet is take characters, and encode them into morse code.
    # this requires a different tree, which should be based on our original BST
    # key is a character, and data is the morse code.
    # you wouldn't want to build this tree with data already in alphabetical order

    print(morse)
if __name__ == "__main__":
    main()