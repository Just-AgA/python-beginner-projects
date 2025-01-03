#Remove first n characters from a string
def remove_chars(word, n):
    print(f"Original string: {word}")
    print(f"New string: ")
    return word[n:]

print(remove_chars("PYnative", 4))