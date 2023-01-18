morse = {
"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
# ...
}

### Code to complete [START] ###

def translate(data):
    try :
        traduction = ""
        for x in data.strip():
            traduction += morse[x] 
        return traduction
    except :
        raise ValueError("Unregistered character !")

