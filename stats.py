def word_count(text):
    words = text.split()
    return len(words)
def char_count(text):
    words = text.lower()
    dict = {}
    for char in words:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict
def sort_on(dict):
    return dict["num"]
def counts_test (counts):
    c_list = []
    for c in counts:
        c_list.append({"char": c, "num": counts[c]})
    c_list.sort(reverse=True, key=sort_on)
    return c_list