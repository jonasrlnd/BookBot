
def get_book_text(path: str):
    with open(path, encoding="utf-8-sig") as f:
        file_contents = f.read()

    return file_contents

def get_num_words(path: str):
    file_contents = get_book_text(path)
    return print(f"Found {len(file_contents.split())} total words")

def sort_on(t: tuple[str, int]) -> int:
    return t[1]

# unsorted dictionary
def get_num_chars(path: str):
    file_contents = get_book_text(path).lower()
    num_chars = {}
    for i in file_contents:
        if i in num_chars:
            num_chars[i] += 1
        else:
            num_chars[i] = 0
    return num_chars

def chars_dict_to_sorted_list(d: dict[str, int]) -> list[tuple[str, int]]:
    el = []
    for i in d:
     el.append( (i, d[i]) )

    sorted_list = sorted(el, reverse=True, key=sort_on)
    return sorted_list
