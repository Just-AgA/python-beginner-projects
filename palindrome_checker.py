#Check if a given string is a palindrome(it is the same word if it's reversed)

def check_palindrome(word):
    #Creat a new variable which holds the reversed string
    new_word = word[::-1]

    #Convert the string to lowercase and compare the reversed string with the origina one
    if new_word.lower() == word.lower():
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")

check_palindrome("cat-tac")