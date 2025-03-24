from stats import book_letter_count, book_word_count, sort_book_letters, print_letter_count
import sys

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()



def main():
    #book_path = 'books/frankenstein.txt'
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    #print(get_book_text('books/frankenstein.txt'))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {book_word_count(book_path)} total words")
        print("--------- Character Count -------")
    #print(book_letter_count(book_path))
        letter_count = sort_book_letters(book_letter_count(book_path))
        print_letter_count(letter_count)
        print("============= END ===============")

main()