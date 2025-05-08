from stats import word_count
from stats import char_count
from stats import counts_test
import sys
def get_book_text(filepath):
    with open (filepath) as f:
        contents = f.read()
    return contents
def main():
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = word_count(text)
    characters = char_count(text)
    c_list = counts_test(characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in c_list:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()