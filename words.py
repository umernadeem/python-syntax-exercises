# def print_upper_words (words):
#     """ prints out all words in uppercase"""
#     for word in words:
#         print(word.upper())


# def print_upper_words (words):
#     """ prints out all words in uppercase"""
#     for word in words:
#         if (word.find("e") == 0):
#             print(word.upper()) 

def print_upper_words (words, must_start_with):
    """ prints out all words in uppercase"""
    for word in words:
        for start in must_start_with:
            if (word.startswith(start)):
                print(word)
        

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})