import sys
from stats import count_words, count_chars, sort_my_dict, get_report, print_dict


def get_book_text(path):
    with open(path) as fn:
        f = fn.read()
        return f

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    textpath = sys.argv[1]

    text = get_book_text(textpath)

    num_words = count_words(text)

    counted_chars = count_chars(text)

    sorted_dict = sort_my_dict(counted_chars)

    sorted_dict_str_repr = print_dict(sorted_dict) 


    ## report
    report = get_report(textpath, num_words, sorted_dict_str_repr)

    print(report)


main()

