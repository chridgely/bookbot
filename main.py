from stats import get_num_words, get_num_chars, sort
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    book_text = get_book_text(path)   
    num = get_num_words(book_text)
    char_dict = get_num_chars(book_text)
    data = sort(char_dict)

    print("========== BOOKBOT ==========") 
    print(f"Analyzing book found at {path}...")
    print("--------- Word Count ---------") 
    print(f"Found {num} total words")
    print("--------- Character Count ---------")
    for d in data:
       print(f"{d['char']}: {d['num']}")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(book_text):
    words = book_text.split()
    return len(words)

main()
