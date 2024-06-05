def main():
    text_path = "books/frankenstein.txt"
    text = get_text(text_path)
    
    word_count = len(text.split())
    letter_count = get_char_count(text)


    print(f"--- Begin report of {text_path} ---")
    print(f"{word_count} words found in the doc\n")

    list_of_dics = dict2list(letter_count)
    list_of_dics.sort(reverse=True, key=sort_on)

    for ch in list_of_dics:
        print(f"The {ch['char']} character was found {ch['count']} times")
    print("--- End report ---")


def get_char_count(text):
    char_count = {}
    lower_text = text.lower()
    for ch in lower_text:
        if ch.isalpha():
            if ch not in char_count:
                char_count[ch] = 0
            else:
                char_count[ch] += 1

    return char_count


def get_text(path):
    with open(path) as f:
        fc = f.read()
    return fc


def dict2list (dict):
    lst = []
    for k in dict:
        tmp_d = {"char" : k, "count" : dict[k]}
        lst.append(tmp_d)
    return lst

def sort_on(dict):
    return dict["count"]

main()
