#!/usr/bin/python3

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    words = word_count(text)
    print(f"{words} words found in the document")
    print("")
    characters = character_count(text)
    final = display(characters)
    for i in final:
        if i['char'].isalpha():
            print(f"The {i['char']} character appears {i['num']} times")
    print("-- End of report --")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    return len(text.split())

def character_count(text):
    dict_char = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char in dict_char:
            dict_char[char] += 1
        else:
            dict_char[char] = 1
    return dict_char

def sort_on(dict):
    return dict["num"]

def display(dict):
    list = []
    for char in dict:
        list.append({"char": char, "num": dict[char]})
    list.sort(reverse=True, key=sort_on)
    return list

main()