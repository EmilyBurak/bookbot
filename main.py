import sys

from stats import get_character_occurrences, get_num_words, sort_character_occurrences


def get_book_text(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
        return file_contents


def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)

    character_occurrences = get_character_occurrences(book_text)
    sorted_characters = sort_character_occurrences(character_occurrences)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for char, count in sorted_characters:
        print(f"{char}: {count}")
    print("============= END ===============")


main()
