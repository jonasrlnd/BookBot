from stats import get_num_words
from stats import get_num_chars
from stats import chars_dict_to_sorted_list
import sys

def print_resport(path):
    unsorted_dict = get_num_chars(path)

    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(get_num_words(path))
    print("--------- Character Count -------")

    for i in chars_dict_to_sorted_list(unsorted_dict):
        if i[0].isalpha():
            print(f"{i[0]}: {i[1]}")

    print("============= END ===============")

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_resport(sys.argv[1])

main()
