def count_words(text):
    return len(text.split())

def count_chars(text):
    char_chart = dict()
    for char in text:
        lower_char = char.lower()
        if lower_char in 'abcdefghijklmnopqrstuvwxyz':
            if lower_char in char_chart.keys():
                char_chart[lower_char] += 1
            else:
                char_chart[lower_char] = 1
    return char_chart


def main():
    with open('books/frankenstein.txt') as f:
        fc = f.read()

        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(fc)} words found in the doc")
        character_chart = count_chars(fc)
        for ch, count in character_chart.items(): 
            print(f"The '{ch}' character was found {count} times")
main()
