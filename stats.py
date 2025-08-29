def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_chars(book_text):
    book_text = book_text.lower()
    count = {}
    for c in book_text:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count

def sort_on(items):
    return items["num"]

def sort(character_dict):
    l = []
    for key in character_dict.keys():
        l.append({
            "char":key, 
            "num" :character_dict[key]
        })
    l.sort(reverse=True,key=sort_on)
    return l
