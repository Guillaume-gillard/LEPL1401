### Code to complete [START] ###

def translate(data, lan):
    translation = ""
    data = data.split(" ")
    for word in data :
        try :
            translation += lan[word.lower()]
        except :
            translation += word
        translation += " "
    return translation.strip() # pour pas avoir l'espace indesirable a la fin de la phrase
