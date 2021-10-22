def print_upper_words (wordlist, startswith):
    """ Prints each word in a list that begins with a given letter on a separate line in capital letters """
    for word in wordlist:
        for char in word:
            if char == startswith:
                # startswith should be a string
                print (word.upper())
