def count_words(text):
    word_count = 0
    words = text.split()
    word_count = len(words)  # Count the number of words in the text.
    return word_count

def count_characters(text):
    # check the amount of each character (from a to z), also symbols and spaces.
    # create a dictionary to store the count of each character
    char_dict = {}
    for char in text:
        if char.isalpha():  # check if the character is a letter
            char = char.lower()  # convert the character to lowercase
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        else:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    return char_dict

def sort_characters(char_dict):
    def sort_on(dict):
        char = list(dict.keys())[0]
        return dict[char]

    char_list = []

    for char, count in char_dict.items():
        char_list.append({char: count})
    
    char_list.sort(key=sort_on, reverse=True)
    
    return char_list