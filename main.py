def count_words(book_name):
    with open("books/" + book_name) as f:
        file_contents = f.read()
        word_count = 0
        words = file_contents.split()
        for word in words:
            word_count += 1
    return word_count


def count_characters(book_name):
    with open("books/" + book_name) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        character_dictionary = {}
        for letter in file_contents:
            if not letter.isalpha():
                continue
            if not letter in character_dictionary:
                character_dictionary[letter] = 0
            character_dictionary[letter] += 1
    return character_dictionary




def report(book_name):
    word_count = count_words(book_name)
    character_count = count_characters(book_name)
    print(f"--- Begin report of books/{book_name} ---")
    print(f"{word_count} words found in the document")
    character_list = chars_dict_to_sorted_list(character_count)
    print("Char list: ", character_list)
    for character in character_list:
        print(f"{character["char"]} character was found {character["num"]} times")


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

report("frankenstein.txt")