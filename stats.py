def get_num_words(book_text):
    words = book_text.split()
    return len(words)


def get_character_occurrences(book_text):
    characters = {}
    for word in book_text.split():
        word = word.strip('.,!?;"()[]').lower()
        for char in word:
            if char.isalpha():
                if char in characters:
                    characters[char] += 1
                else:
                    characters[char] = 1
    return characters


def sort_character_occurrences(character_dict):
    final_list = []
    for char, count in character_dict.items():
        if char.isalpha():
            final_list.append((char, count))
        else:
            continue
    final_list.sort(reverse=True, key=lambda x: x[1])
    return final_list
