def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_words = get_words(text)
    print(f"There are {num_words} in the text.")
    chars_dict = count_characters(text)
    print(chars_dict)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")



def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()

def get_words(text):
    words = text.split()
    return (len(words))

def count_characters(text):
    dict = {}
    for word in text:
        lowered = word.lower()
        if lowered in dict:
            dict[lowered] += 1
        else:
            dict[lowered] = 1
    return dict
    
def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



main()