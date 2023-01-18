### Code to complete [START] ###

def create_dictionary(filename):
    d = {}
    with open(filename, "r") as file:
        for line in file :
            for word in line.split(' '):
                if word in d :
                    d[word] += 1
                else :
                    d[word] = 1
        return d
    
def occ(dictionary, word):
    try :
        return dictionary[word]
    except KeyError: 
        return 0
