def extract(code):
    """gives the nature of each element of a string"""
    pass

def treatment(code):
    """transform a suite of elements into a pattern"""
    pass

def collect(file):
    occurences = {"number" : 0, "vowel-up" : 0, "vowel-low" : 0, "consonant-up" : 0, "consonant-low" : 0}
    with open(file, "r") as file :
        for text in file.readlines() :
            line = text.strip().split()
            for word in line :
                pattern = treatment(word)
                for j in pattern.split():
                    info = j.split("*")
                    occurences[info[0]] += info[1]
    return occurences
