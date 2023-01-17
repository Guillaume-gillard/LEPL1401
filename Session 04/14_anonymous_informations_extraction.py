### Code to complete [START] ###

import string 
    
def extract(code):
    code = str(code)
    composition = ""
    alphabet = string.ascii_lowercase + string.ascii_uppercase # voir docu python
    number = "1234567890"
    vowel = "aeiouy"
    vowel_up = vowel.upper()
    consonant_upper = "B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z"
    consonant = consonant_upper.lower()
    for i in code:
        if i in vowel_up :
            composition += "vowel-up "
        if i in vowel :
            composition += "vowel-low "
        if i in consonant :
            composition += "consonant-low "
        if i in consonant_upper :
            composition += "consonant-up "
        elif i in number :
            composition += "number "
    return composition
