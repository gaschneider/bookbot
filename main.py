def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_content(book_path)
    book_words = count_words(book_content)
    book_amount_of_chars = count_char(book_content)
    print_report(book_path, book_words, book_amount_of_chars)

def get_book_content(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(string_to_count):
    words = string_to_count.split()
    return len(words)

def count_char(string_to_count):
    char_count = {}
    for c in string_to_count:
        lower_c = c.lower()
        if lower_c not in char_count:
            char_count[lower_c] = 0

        char_count[lower_c] += 1

    return char_count

def convert_chars_dict_to_list(book_amount_of_chars):
    list = []
    for c in book_amount_of_chars:
        list.append({"char": c, "count": book_amount_of_chars[c]})
    
    return list

def sort_on_count(dict):
    return dict["count"]

def print_report(filepath, book_words, book_amount_of_chars):
    print(f"--- Begin report of {filepath} ---")
    print(f"{book_words} words found in the document")
    print()

    sorted_amount_of_chars = convert_chars_dict_to_list(book_amount_of_chars)
    sorted_amount_of_chars.sort(reverse=True, key=sort_on_count)
    
    for item in sorted_amount_of_chars:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["count"]} times")

    print("--- End report ---")

main()