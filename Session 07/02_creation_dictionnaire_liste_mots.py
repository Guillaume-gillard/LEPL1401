### Code to complete [START] ###


def create_index(list_of_words):
    d = {}
    pos = 0
    for words in list_of_words :
        if words not in d :
            d[words] = [pos]
        else :
            d[words] += [pos]
        pos += 1
    return d