from stats import count_words
from stats import count_characters
from stats import sort_characters
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
        return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 bookbot.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_count = count_characters(text)
    sorted_char_count = sort_characters(char_count)
    print("--------- Character Count -------")
    for sorted_char_dict in sorted_char_count:
        key = list(sorted_char_dict.keys())[0]
        print(f"{key}: {sorted_char_dict[key]}")
    print("============= END ===============")

main()