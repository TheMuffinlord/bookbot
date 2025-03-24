def book_word_count(filepath):
    word_count = 0
    with open(filepath) as book:
        book_to_count = book.read()
    split_book = book_to_count.split()
    for word in split_book:
        word_count+=1
    return word_count

def book_letter_count(filepath):
    all_counted_letters = {}
    with open(filepath) as book:
        book_to_count = book.read()
    lower_book = book_to_count.lower()
    for letter in lower_book:
        if letter not in all_counted_letters:
            all_counted_letters[letter] = 1
        else:
            all_counted_letters[letter]+=1
    return all_counted_letters

def sort_by(dict):
    return dict["count"]

def sort_book_letters(book_letters):
    unsorted_letters = []
    for l in book_letters:
        unsorted_letters.append({"letter": l, "count": book_letters[l]})
    unsorted_letters.sort(key=sort_by, reverse=True)
    return unsorted_letters

def print_letter_count(letters):
    for l in letters:
        if l["letter"].isalpha():
            print(f"{l['letter']}: {l['count']}")
