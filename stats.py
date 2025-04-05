def count_words(text):
    return len(text.split())

def count_chars(text):
    char_set = dict()
    for t in text:
        t = t.lower()
        if t in char_set:
            char_set[t] += 1
        else:
            char_set[t] = 1
    return char_set


def sort_tup(t):
    return t[1]


def sort_my_dict(d):
    ld = list(d.items())
    ld.sort(reverse=True, key=sort_tup)
    return dict(ld)


def print_dict(d):
    res = ""
    for k,v in d.items():
        if k.isalpha():
            res += f"{k}: {v}\n"
    return res


def get_report(path:str, num_words:int, sorted_chars:str):
    printout = """\
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------
{sorted_chars}
============= END ===============\
    """.format(path=path, words=num_words, sorted_chars=sorted_chars)

    return printout
 

    
